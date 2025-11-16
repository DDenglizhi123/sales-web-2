from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Products
from django.urls import reverse_lazy
from .forms import ProductForm
from django.db.models import Q
# Create your views here.
class ProductListView(ListView):
    model = Products
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    fields = ['item_name', 'price', 'unit', 'stock_quantity', 'item_number', 'keyword1', 'keyword2', 'keyword3', 'weight_in_kg', 'packing_L', 'packing_W', 'packing_H']
    paginate_by = 20  # Number of customers per page
    
    #查询功能
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(item_name__icontains=search) |
                Q(keyword1__icontains=search) |
                Q(keyword2__icontains=search) |
                Q(keyword3__icontains=search)
            )
        return queryset


class ProductCreateView(CreateView):
    model = Products
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('item_list')




class ProductUpdateView(UpdateView):
    # model = Products
    # template_name = 'products/product_form.html'
    # context_object_name = 'product'
    # fields = ['item_name', 'price', 'keyword1', 'keyword2', 'keyword3', 'item_number', 'unit', 'stock_quantity', 'weight_in_kg', 'packing_L', 'packing_W', 'packing_H']
    # success_url = '/item_list/'  # Redirect to the customer list after successful update
    pass

class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'products/product_delete.html'
    context_object_name = 'products'
    success_url = reverse_lazy('item_list')  # Redirect to the customer list after successful deletion