from django.urls import path
from .views import product_list
urlpatterns = [
    path('',product_list, name='item_list'),
    # path('create/', ProductCreateView.as_view(), name='item_create'),
    # path('update/<int:pk>/', ProductUpdateView.as_view(), name='item_update'),
    # path('delete/<int:pk>/', ProductDeleteView.as_view(), name='item_delete'),
]
