from django.urls import path
from .views import product_list, ProductCreateView
urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
]
