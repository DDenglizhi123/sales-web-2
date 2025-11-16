from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'name_in_short', 'TIN', 'VRN', 'contact_person', 'phone', 'emial', 'address_line1', 'address_line2', 'business_type']
