from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [
    path('',ProductListView.as_view(), name='item_list'),
    path('create/', ProductCreateView.as_view(), name='item_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='item_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='item_delete'),
]
