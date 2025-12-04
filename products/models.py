from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    item_name = models.CharField(max_length=500, unique=False, blank=False, null=False)
<<<<<<< HEAD
    base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
=======
    specification = models.CharField(max_length=200, unique=False, blank=True, null=True)
    chinese_name = models.CharField(max_length=500, unique=False, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    item_type = [
        ('C', 'Cable'),
        ('T', 'Transformer'),
        ('A', 'Accessories'),
        ('P', 'Concrete poles'),
        ('S', 'Spare parts'),
        ('R', 'Raw Materials'),
        ('O', 'Others'),
    ]
    product_type = models.CharField(max_length=15, blank=False, null=False, help_text='Cable, Transformer, Accessories, Concrete poles, Spare parts, Raw Materials', choices=item_type, default='Cable')
    item_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
>>>>>>> 48d4184 (update)
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
<<<<<<< HEAD
    unit = models.CharField(max_length=10, choices=unit_type, blank=False, null=False, unique=False)
    stock_quantity = models.CharField(max_length=13, blank=True, help_text='Optional')
=======
    unit = models.CharField(max_length=10, choices=unit_type, blank=False, null=False)
    stock_quantity = models.CharField(max_length=13, blank=True, help_text='Optional')
    weight_in_kg = models.CharField(max_length=10, blank=True, null=True)
    packing_L = models.IntegerField(blank=True, null=True, help_text="Optional field for integer values")
    packing_W = models.IntegerField(blank=True, null=True, help_text="Optional field for integer values")
    packing_H = models.IntegerField(blank=True, null=True, help_text="Optional field for integer values")
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_created', null=True)
>>>>>>> 48d4184 (update)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.item_name
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
