from django.db import models

# Create your models here.
class Delivery(models.Model):
    order_number
    items
    delivery_date
    