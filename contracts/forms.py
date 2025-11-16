from django import forms
from .models import Contracts

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = ['contractor', 'contract_number', 'site_name', 'project_name', 'lot_number', 'contract_value', 'payment_method', 'credit_days', 'contract_currency', 'sign_date', 'contract_end_date']
