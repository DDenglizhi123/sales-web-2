from django import forms
from .models import Contracts

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts
<<<<<<< HEAD
        fields = '__all__'
        widgets = {
            'sign_date': forms.DateInput(attrs={'type': 'date'}),
            'contract_end_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_type': forms.Select(attrs={'id': 'id_payment_type'}),
            'credit_days': forms.NumberInput(attrs={
                'id': 'id_credit_days',
                'placeholder': 'Enter Credit Days',
                'style': 'display:none;'  # 初始隐藏
            }),
        }
=======
        fields = ['contractor', 'contract_number', 'site_name', 'project_name', 'lot_number', 'contract_value', 'payment_method', 'credit_days', 'contract_currency', 'sign_date', 'contract_end_date']
>>>>>>> 558c915 (update)
