from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    item_name = models.CharField(max_length=500, unique=False, blank=False, null=False)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    unit_type = [
        ('M', 'M'),
        ('KM', 'KM'),
        ('KG', 'KG'),
        ('PK', 'Package'),
        ('LT', 'Liter'),
        ('PC', 'Piece'),
        ('TSH', 'TSH'),
        ('SET', 'SET'),
    ]
    unit = models.CharField(max_length=10, choices=unit_type, blank=False, null=False, unique=False)
    stock_quantity = models.CharField(max_length=13, blank=True, help_text='Optional')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.item_name
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
