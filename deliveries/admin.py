from django.contrib import admin
from .models import Delivery, DeliveryItem

# Register your models here.

class DeliveryItemInline(admin.TabularInline):
    """发货项内联编辑"""
    model = DeliveryItem
    extra = 1
    fields = ('order_item', 'delivered_quantity', 'notes')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    """发货单管理"""
    list_display = ('delivery_number', 'order', 'customer', 'delivery_date', 'status', 'created_at')
    list_filter = ('status', 'delivery_date', 'created_at')
    search_fields = ('delivery_number', 'order__order_number', 'customer__name')
    date_hierarchy = 'delivery_date'
    readonly_fields = ('created_at', 'updated_at')
    inlines = [DeliveryItemInline]
    
    fieldsets = (
        ('基本信息', {
            'fields': ('delivery_number', 'order', 'customer', 'delivery_date', 'status')
        }),
        ('其他信息', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(DeliveryItem)
class DeliveryItemAdmin(admin.ModelAdmin):
    """发货项管理"""
    list_display = ('delivery', 'order_item', 'delivered_quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('delivery__delivery_number', 'order_item__product__item_name')
    readonly_fields = ('created_at', 'updated_at')
