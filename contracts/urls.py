from django.urls import path
<<<<<<< HEAD
from .views import ContractListView, ContractCreateView,ContractUpdateView, ContractDeleteView
urlpatterns = [
    path('',ContractListView.as_view(), name='contract_list'),
    path('create/', ContractCreateView.as_view(), name='contract_create'),
    path('update/<int:pk>', ContractUpdateView.as_view(), name='contract_update'),
    path('delete/<int:pk>', ContractDeleteView.as_view(), name='contract_delete'),
=======
from .views import ContractListView, ContractCreateView, ContractDeleteView, ContractUpdateView
urlpatterns = [
    path('',ContractListView.as_view(), name='contract_list'),
    path('create/', ContractCreateView.as_view(), name='contract_create'),
    path('update/<int:pk>/', ContractUpdateView.as_view(), name='contract_update'),
    path('delete/<int:pk>/', ContractDeleteView.as_view(), name='contract_delete'),
>>>>>>> 558c915 (update)
]
