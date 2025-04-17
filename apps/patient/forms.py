from django import forms
from .models import ModelPacient


class PacientForm(forms.ModelForm):
    class Meta:
        model = ModelPacient
        fields = [
            'name',
            'birth_date',
            'gender',
            'plan_card',
            'phone',
            'guardian_name',
        ]
        labels = {
            'name': 'Nome Completo',
            'birth_date': 'Data de Nascimento',
            'gender': 'Gênero',
            'plan_card': 'Carteira do Plano',
            'phone': 'Telefone',
            'guardian_name': 'Nome do Responsável',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control w-100'}),
            'gender': forms.Select(attrs={'class': 'form-control w-100'}),
            'plan_card': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'phone': forms.TextInput(attrs={'placeholder': '(99)99999-9999', 'class': 'form-control w-100'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'plan_card': 'Número da carteira do plano de saúde',
        }
        