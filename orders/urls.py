
from django.urls import path
from .views import order_list, order_details, customer_orders, create_order

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='order_create'),
    path('order_details/<int:pk>/', order_details, name='order_details'),
    path('customer/<int:customer_id>/', customer_orders, name='customer_orders'),
]
