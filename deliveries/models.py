from django.db import models
from orders.models import Order, OrderItem
from customers.models import Customer

# Create your models here.
class Delivery(models.Model):
    """发货单模型"""
    delivery_number = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name='发货单号')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='deliveries', verbose_name='订单')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='deliveries', verbose_name='客户')
    delivery_date = models.DateField(verbose_name='发货日期')
    vehicle_number = models.CharField(max_length=50, verbose_name='货车号码', default='')
    driver_phone = models.CharField(max_length=20, verbose_name='司机电话', default='')
    driver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='司机姓名')
    
    STATUS_CHOICES = [
        ('PENDING', '待发货'),
        ('IN_TRANSIT', '运输中'),
        ('DELIVERED', '已送达'),
        ('CANCELLED', '已取消'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name='状态'
    )
    
    notes = models.TextField(blank=True, null=True, verbose_name='备注')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    def __str__(self):
        delivery_num = self.delivery_number if self.delivery_number else "未填写"
        return f"发货单号: {delivery_num} - 订单: {self.order.order_number}"
    
    class Meta:
        verbose_name = '发货单'
        verbose_name_plural = '发货单'
        ordering = ['-delivery_date', '-created_at']
        db_table = 'deliveries'


class DeliveryItem(models.Model):
    """发货项模型"""
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='items', verbose_name='发货单')
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='delivery_items', verbose_name='订单项')
    delivered_quantity = models.PositiveIntegerField(verbose_name='发货数量')
    notes = models.TextField(blank=True, null=True, verbose_name='备注')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    def __str__(self):
        delivery_num = self.delivery.delivery_number if self.delivery.delivery_number else "未填写"
        return f"{delivery_num} - {self.order_item.product} ({self.delivered_quantity})"
    
    class Meta:
        verbose_name = '发货项'
        verbose_name_plural = '发货项'
        ordering = ['-created_at']
        db_table = 'delivery_items'