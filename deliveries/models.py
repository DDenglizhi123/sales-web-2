from django.db import models
from orders.models import Order, OrderItem
from customers.models import Customer

# Create your models here.
class Delivery(models.Model):
    """发货单模型"""
    delivery_number = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name='Delivery Number')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='deliveries', verbose_name='Order')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='deliveries', verbose_name='Customer')
    delivery_date = models.DateField(verbose_name='Delivery Date')
    vehicle_number = models.CharField(max_length=50, verbose_name='Vehicle Number', default='')
    driver_phone = models.CharField(max_length=20, verbose_name='Driver Phone', default='')
    driver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Driver Name')
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name='Status'
    )
    
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    def __str__(self):
        delivery_num = self.delivery_number if self.delivery_number else "Not filled"
        return f"Delivery note number: {delivery_num} - Order: {self.order.order_number}"
    
    class Meta:
        verbose_name = 'Delivery Order'
        verbose_name_plural = 'Delivery Orders'
        ordering = ['-delivery_date', '-created_at']
        db_table = 'deliveries'


class DeliveryItem(models.Model):
    """发货项模型"""
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='items', verbose_name='Delivery Order')
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='delivery_items', verbose_name='Order Item')
    delivered_quantity = models.PositiveIntegerField(verbose_name='Delivered Quantity')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    def __str__(self):
        delivery_num = self.delivery.delivery_number if self.delivery.delivery_number else "Not filled"
        return f"{delivery_num} - {self.order_item.product} ({self.delivered_quantity})"
    
    class Meta:
        verbose_name = 'Delivery Item'
        verbose_name_plural = 'Delivery Items'
        ordering = ['-created_at']
        db_table = 'delivery_items'