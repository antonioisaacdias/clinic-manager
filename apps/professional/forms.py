from django import forms
from .models import ModelSpecialty

class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = ModelSpecialty
        fields = ['name', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Nome da especialidade',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
        labels = {
            'name': 'Nome',
            'is_active': 'Ativo',
        }
