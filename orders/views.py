from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.db.models import Q, Sum
from deliveries.models import DeliveryItem
from customers.models import Customer

# Create your views here.
def order_list(request):
    # Searching function
    query = request.GET.get('search', '').strip()
    if query:
        orders = Order.objects.filter(
            Q(customer__name__icontains=query)
            | Q(order_number__icontains=query)
            | Q(ordered__product__item_name__icontains=query)
        ).distinct()
    else:
        orders = Order.objects.all()

    return render(request, 'orders/order_list.html', {'orders': orders, 'query': query})

def order_details(request, pk):
    order_items = OrderItem.objects.filter(order=pk)
    order = Order.objects.get(id=pk)
    customer_name = order.customer.name
    order_number = order.order_number
    
    # 计算每个订单项的已发货数量和剩余数量
    order_items_with_delivery = []
    for item in order_items:
        # 计算该订单项已发货的总数量
        delivered_total = DeliveryItem.objects.filter(
            order_item=item
        ).aggregate(total=Sum('delivered_quantity'))['total'] or 0
        
        # 剩余可发货数量 = 订单数量 - 已发货数量
        remaining_quantity = item.quantity - delivered_total
        
        order_items_with_delivery.append({
            'order_item': item,
            'delivered_total': delivered_total,
            'remaining_quantity': max(0, remaining_quantity)
        })
    
    contexts = {
        'order_items_with_delivery': order_items_with_delivery,
        'customer_name': customer_name,
        'order_number': order_number,
        'order': order,
        }
    return render(request, 'orders/order_details.html', contexts)

def delivery_order(request):
    return render(request, 'orders/delivery_order.html')

def customer_orders(request, customer_id):
    """显示特定客户的所有订单"""
    customer = get_object_or_404(Customer, id=customer_id)
    
    # 搜索功能
    query = request.GET.get('search', '').strip()
    if query:
        orders = Order.objects.filter(
            customer=customer
        ).filter(
            Q(order_number__icontains=query)
            | Q(ordered__product__item_name__icontains=query)
        ).distinct()
    else:
        orders = Order.objects.filter(customer=customer)
    
    context = {
        'customer': customer,
        'orders': orders,
        'query': query,
    }
    return render(request, 'orders/customer_orders.html', context)