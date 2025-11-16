from django import forms
from .models import Delivery

class DeliveryForm(forms.ModelForm):
    """发货单表单"""
    delivery_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='发货日期',
        required=True
    )
    vehicle_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='货车号码',
        max_length=50,
        required=True
    )
    driver_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='司机电话',
        max_length=20,
        required=True
    )
    driver_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='司机姓名',
        max_length=100,
        required=False
    )
    delivery_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='发货单号',
        max_length=20,
        required=False
    )
    
    class Meta:
        model = Delivery
        fields = ['delivery_date', 'vehicle_number', 'driver_phone', 'driver_name', 'delivery_number']
