from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    item_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Item Name',
        max_length=500,
        required=True
    )
    base_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        label='Base Price',
        max_digits=10,
        decimal_places=2,
        required=True
    )
    unit = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Unit',
        choices=[
            ('M', 'M'),
            ('KM', 'KM'),
            ('KG', 'KG'),
            ('PK', 'Package'),
            ('LT', 'Liter'),
            ('PC', 'Piece'),
            ('TSH', 'TSH'),
            ('SET', 'SET'),
        ],
        required=True
    )
    stock_quantity = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Stock Quantity',
        max_length=13,
        required=False,
        help_text='Optional'
    )
    
    class Meta:
        model = Products
        fields = ['item_name', 'base_price', 'unit', 'stock_quantity']