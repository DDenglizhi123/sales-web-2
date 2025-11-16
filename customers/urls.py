from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
urlpatterns = [
    path('',CustomerListView.as_view(), name='customer_list'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
]
