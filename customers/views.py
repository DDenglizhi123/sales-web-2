from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy
from .forms import CustomerForm
from django.db.models import Q
# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    fields = ['name', 'name_in_short', 'TIN', 'VRN', 'contact_person', 'phone', 'emial', 'address_line1', 'address_line2', 'business_type']
    paginate_by = 10  # Number of customers per page
    
    #查询功能
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(name_in_short__icontains=search) |
                Q(TIN__icontains=search) |
                Q(VRN__icontains=search) |
                Q(business_type__icontains=search)
            )
        return queryset


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')




class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    context_object_name = 'customer'
    fields = ['name', 'name_in_short', 'TIN', 'VRN', 'contact_person', 'phone', 'emial', 'address_line1', 'address_line1', 'business_type']
    success_url = '/customers/'  # Redirect to the customer list after successful update

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')  # Redirect to the customer list after successful deletion