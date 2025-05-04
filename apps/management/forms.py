from django import forms
from .models import ModelPlan

class PlanForm(forms.ModelForm):
    class Meta:
        model = ModelPlan
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control w-100', 'rows': 6}),
        }
        labels = {
            'name': 'Nome do Plano',
            'description': 'Descrição',
        }
        