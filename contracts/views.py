from django.shortcuts import render
from .models import Contracts
<<<<<<< HEAD
from customers.models import Customer
=======
>>>>>>> 558c915 (update)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ContractForm
from  django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class ContractListView(ListView):
    model = Contracts
    template_name = 'contracts/contract_list.html'
    context_object_name = 'contracts'
    fields = ['id', 'contract_number', 'contractor', 'lot_number', 'payment_method', 'contract_value', 'credit_days', 'created_at', 'updated_at']
    paginate_by = 20  # Number of customers per page
    
    #查询功能
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(contractor__icontains=search) |
                Q(contract_number__icontains=search) 
            )
        return queryset

    
class ContractCreateView(CreateView):
    model = Contracts
    template_name = 'contracts/contract_form.html'
    form_class = ContractForm
    success_url = reverse_lazy('contract_list')
    
class ContractUpdateView(UpdateView):
    model = Contracts
    template_name = 'contracts/contract_form.html'
    context_object_name = 'contracts'
<<<<<<< HEAD
    fields = '__all__'
    success_url = '/contracts/'  # Redirect to the contract list after successful update
=======
    fields = []
    success_url = reverse_lazy('contract_list')  # Redirect to the customer list after successful update
>>>>>>> 558c915 (update)

class ContractDeleteView(DeleteView):
    model = Contracts
    template_name = 'contracts/contract_delete.html'
    context_object_name = 'contracts'
<<<<<<< HEAD
    success_url = reverse_lazy('contract_list')  # Redirect to the contract list after successful deletion
=======
    success_url = reverse_lazy('contract_list')  # Redirect to the customer list after successful deletion
>>>>>>> 558c915 (update)
