from django import forms
from .models import ModelSpecialty, ModelProfessional

class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = ModelSpecialty
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Nome da especialidade',
            }),
        }
        labels = {
            'name': 'Nome',
        }
        
