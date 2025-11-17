from django import forms
from .models import Order, OrderItem
from customers.models import Customer
from products.models import Products

class OrderForm(forms.ModelForm):
    order_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Order Number',
        max_length=20,
        required=True
    )
    customer = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Customer.objects.all(),
        label='Customer',
        required=True,
        empty_label='Select a customer'
    )
    
    class Meta:
        model = Order
        fields = ['order_number', 'customer']


class OrderItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Products.objects.all(),
        label='Product',
        required=True,
        empty_label='Select a product'
    )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        label='Quantity',
        required=True,
        min_value=1
    )
    unit_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        label='Unit Price',
        max_digits=10,
        decimal_places=2,
        required=True,
        min_value=0
    )
    
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'unit_price']

