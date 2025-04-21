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

class ProfessionalForm(forms.ModelForm):
    
    class Meta:
        model = ModelProfessional
        fields = [
            'name', 'birth_date', 'gender', 'cpf', 'email', 'registration_number', 'specialties', 'phone', 'user'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control w-100'}),
            
            'gender': forms.Select(attrs={'class': 'form-select form-control w-100'}),
            
            'cpf': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Apenas números'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control w-100'}),
            
            'registration_number': forms.TextInput(attrs={'class': 'form-control w-100'}),
            
            'specialties': forms.CheckboxSelectMultiple(),
            
            'phone': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': '(DD)999999999', 'multiple': True, }),
            
            'user': forms.Select(attrs={'class': 'form-select form-control w-100'}),
        }
        labels = {
            'name': 'Nome completo',
            'birth_date': 'Data de nascimento',
            'gender': 'Gênero',
            'cpf': 'CPF',
            'email': 'E-mail',
            'registration_number': 'Número de registro profissional',
            'phone': 'Telefone',
            'user': 'Usuário vinculado',
        }
        
