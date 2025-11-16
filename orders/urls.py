
from django.urls import path
from .views import order_list, order_details, customer_orders

urlpatterns = [
    path('', order_list, name='order_list'),
    path('order_details/<int:pk>/', order_details, name='order_details'),
    path('customer/<int:customer_id>/', customer_orders, name='customer_orders'),
]
