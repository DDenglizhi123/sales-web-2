from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Q
from django.utils import timezone
from .models import Delivery, DeliveryItem
from .forms import DeliveryForm
from orders.models import Order, OrderItem

def create_delivery(request):
    """创建发货单视图"""
    order_id = request.GET.get('order_id')
    order_items_str = request.GET.get('order_items', '')
    
    if not order_id:
        messages.error(request, 'Missing order ID')
        return redirect('order_list')
    
    order = get_object_or_404(Order, id=order_id)
    
    # 解析选中的订单项ID
    if order_items_str:
        order_item_ids = [int(id) for id in order_items_str.split(',') if id]
        selected_order_items = OrderItem.objects.filter(id__in=order_item_ids, order=order)
    else:
        selected_order_items = OrderItem.objects.none()
    
    # 计算每个订单项的剩余可发货数量
    order_items_with_remaining = []
    for item in selected_order_items:
        # 计算该订单项已发货的总数量
        delivered_total = DeliveryItem.objects.filter(
            order_item=item
        ).aggregate(total=Sum('delivered_quantity'))['total'] or 0
        
        # 剩余可发货数量 = 订单数量 - 已发货数量
        remaining_quantity = item.quantity - delivered_total
        order_items_with_remaining.append({
            'order_item': item,
            'delivered_total': delivered_total,
            'remaining_quantity': max(0, remaining_quantity)  # 确保不为负数
        })
    
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        # 确保在POST时也计算剩余数量（用于表单验证失败时显示）
        if not order_items_with_remaining:
            for item in selected_order_items:
                delivered_total = DeliveryItem.objects.filter(
                    order_item=item
                ).aggregate(total=Sum('delivered_quantity'))['total'] or 0
                remaining_quantity = item.quantity - delivered_total
                order_items_with_remaining.append({
                    'order_item': item,
                    'delivered_total': delivered_total,
                    'remaining_quantity': max(0, remaining_quantity)
                })
        
        if form.is_valid():
            # 验证发货数量
            order_item_ids = request.POST.getlist('order_item_ids')
            quantities = request.POST.getlist('quantities')
            validation_errors = []
            has_valid_quantity = False  # 检查是否至少有一个数量大于0
            
            for item_id, quantity in zip(order_item_ids, quantities):
                if item_id and quantity:
                    order_item = get_object_or_404(OrderItem, id=int(item_id))
                    quantity = int(quantity)
                    
                    # 计算剩余可发货数量
                    delivered_total = DeliveryItem.objects.filter(
                        order_item=order_item
                    ).aggregate(total=Sum('delivered_quantity'))['total'] or 0
                    remaining_quantity = order_item.quantity - delivered_total
                    
                    if quantity > 0:
                        has_valid_quantity = True
                        if quantity > remaining_quantity:
                            validation_errors.append(
                                f"{order_item.product.item_name}: 发货数量({quantity})不能超过剩余可发货数量({remaining_quantity})"
                            )
                    # 如果数量为0，不显示错误（允许用户不发货某些产品）
            
            # 确保至少有一个产品的发货数量大于0
            if not has_valid_quantity:
                validation_errors.append("至少需要为一个产品输入大于0的发货数量")
            
            if validation_errors:
                for error in validation_errors:
                    messages.error(request, error)
                # 重新计算剩余数量（以防万一）
                order_items_with_remaining = []
                for item in selected_order_items:
                    delivered_total = DeliveryItem.objects.filter(
                        order_item=item
                    ).aggregate(total=Sum('delivered_quantity'))['total'] or 0
                    remaining_quantity = item.quantity - delivered_total
                    order_items_with_remaining.append({
                        'order_item': item,
                        'delivered_total': delivered_total,
                        'remaining_quantity': max(0, remaining_quantity)
                    })
                context = {
                    'form': form,
                    'order': order,
                    'order_items_with_remaining': order_items_with_remaining,
                }
                return render(request, 'deliveries/delivery_form.html', context)
            
            # 验证通过，创建发货单
            delivery = form.save(commit=False)
            delivery.order = order
            delivery.customer = order.customer
            delivery.status = 'DELIVERED'  # 提交时状态设为已送达
            delivery.save()
            
            # 创建发货项（只创建数量大于0的）
            for item_id, quantity in zip(order_item_ids, quantities):
                if item_id and quantity:
                    quantity = int(quantity)
                    if quantity > 0:  # 只创建数量大于0的发货项
                        order_item = get_object_or_404(OrderItem, id=int(item_id))
                        DeliveryItem.objects.create(
                            delivery=delivery,
                            order_item=order_item,
                            delivered_quantity=quantity
                        )
            
            return redirect('delivery_success', pk=delivery.id)
        else:
            # 表单验证失败，显示错误
            context = {
                'form': form,
                'order': order,
                'order_items_with_remaining': order_items_with_remaining,
            }
            return render(request, 'deliveries/delivery_form.html', context)
    else:
        # 设置默认发货日期为今天
        today = timezone.now().date()
        form = DeliveryForm(initial={'delivery_date': today})
    
    context = {
        'form': form,
        'order': order,
        'order_items_with_remaining': order_items_with_remaining,
    }
    return render(request, 'deliveries/delivery_form.html', context)


def delivery_success(request, pk):
    """发货单成功页面"""
    delivery = get_object_or_404(Delivery, id=pk)
    delivery_items = DeliveryItem.objects.filter(delivery=delivery)
    
    # 生成可复制内容（使用制表符分隔）
    copy_content_parts = []
    copy_content_parts.append(f"发货单号\t{delivery.delivery_number or '未填写'}")
    copy_content_parts.append(f"订单号\t{delivery.order.order_number}")
    copy_content_parts.append(f"客户\t{delivery.customer.name if delivery.customer else '未填写'}")
    copy_content_parts.append(f"发货日期\t{delivery.delivery_date}")
    copy_content_parts.append(f"货车号码\t{delivery.vehicle_number}")
    copy_content_parts.append(f"司机电话\t{delivery.driver_phone}")
    if delivery.driver_name:
        copy_content_parts.append(f"司机姓名\t{delivery.driver_name}")
    copy_content_parts.append("")
    copy_content_parts.append("产品信息：")
    # 确保产品信息正确显示
    if delivery_items.exists():
        for item in delivery_items:
            copy_content_parts.append(f"{item.order_item.product.item_name}, {item.delivered_quantity}{item.order_item.product.unit};")
    else:
        copy_content_parts.append("无产品信息")
    if delivery.notes:
        copy_content_parts.append("")
        copy_content_parts.append(f"备注\t{delivery.notes}")
    
    copy_content = "\n".join(copy_content_parts)
    
    context = {
        'delivery': delivery,
        'delivery_items': delivery_items,
        'copy_content': copy_content,
    }
    return render(request, 'deliveries/delivery_success.html', context)


def delivery_list(request):
    """发货单列表视图"""
    # 搜索功能
    query = request.GET.get('search', '').strip()
    if query:
        deliveries = Delivery.objects.filter(
            Q(delivery_number__icontains=query)
            | Q(order__order_number__icontains=query)
            | Q(customer__name__icontains=query)
            | Q(vehicle_number__icontains=query)
        ).distinct()
    else:
        deliveries = Delivery.objects.all()
    
    # 处理确认发货（更新发货单号）
    if request.method == 'POST':
        delivery_id = request.POST.get('delivery_id')
        delivery_number = request.POST.get('delivery_number', '').strip()
        
        if delivery_id and delivery_number:
            try:
                delivery = Delivery.objects.get(id=delivery_id)
                # 检查发货单号是否已存在
                if Delivery.objects.filter(delivery_number=delivery_number).exclude(id=delivery_id).exists():
                    messages.error(request, f'发货单号 {delivery_number} 已存在，请使用其他发货单号')
                else:
                    delivery.delivery_number = delivery_number
                    delivery.status = 'DELIVERED'  # 确认已发货
                    delivery.save()
                    messages.success(request, f'发货单号 {delivery_number} 已确认')
            except Delivery.DoesNotExist:
                messages.error(request, '发货单不存在')
        else:
            messages.error(request, '请填写发货单号')
        
        # 重新获取列表（保持搜索条件）
        if query:
            deliveries = Delivery.objects.filter(
                Q(delivery_number__icontains=query)
                | Q(order__order_number__icontains=query)
                | Q(customer__name__icontains=query)
                | Q(vehicle_number__icontains=query)
            ).distinct()
        else:
            deliveries = Delivery.objects.all()
    
    context = {
        'deliveries': deliveries,
        'query': query,
    }
    return render(request, 'deliveries/delivery_list.html', context)