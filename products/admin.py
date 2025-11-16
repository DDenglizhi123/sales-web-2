from django.contrib import admin
from .models import Products
<<<<<<< HEAD

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'price', 'unit', 'product_type', 'show_date_created_at', 'show_date_updated_at','stock_quantity',)
    search_fields = ('item_name',)
    list_filter = ('product_type', 'product_type',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    def show_date_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')  # 只显示日期
    def show_date_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d')  # 只显示日期
=======
# Register your models here.
admin.site.register(Products)
>>>>>>> 558c915 (update)
