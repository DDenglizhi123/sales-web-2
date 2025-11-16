from django.urls import path
from .views import create_delivery, delivery_success, delivery_list

urlpatterns = [
    path('', delivery_list, name='delivery_list'),
    path('create/', create_delivery, name='create_delivery'),
    path('success/<int:pk>/', delivery_success, name='delivery_success'),
]
