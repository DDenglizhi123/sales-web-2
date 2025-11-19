from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, unique=True)
    name_in_short = models.CharField(max_length=10, blank=True, null=True)
    TIN = models.CharField(max_length=11, help_text='eg. xxx-xxx-xxx', blank=True, null=True, unique=True)
    VRN = models.CharField(max_length=12, help_text='eg. xx-xxxxxx-x', blank=True, null=True, unique=True)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    emial = models.EmailField(blank=True, null=True)
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)

    BUSINESS_TYPE_CHOICES = [
        ('REA', 'REA Contractor'),
        ('GOV', 'Government'),
        ('OTH', 'Undefined'),
    ]
    business_type = models.CharField(
        max_length=3,
        choices=BUSINESS_TYPE_CHOICES,
        default='OTH',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    # last_order_date = models.DateTimeField(blank=True, null=True)
    


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        # ordering = ['-last_order_date']