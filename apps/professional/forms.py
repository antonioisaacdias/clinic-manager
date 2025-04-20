from django import forms
from .models import ModelSpecialty, ModelProfessional
from django_select2.forms import Select2MultipleWidget

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
        
from django import forms
from .models import ModelProfessional

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = ModelProfessional
        fields = [
            'name', 'birth_date', 'gender', 'cpf', 'email', 'registration_number',
            'phone', 'specialties', 'user'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control w-100'}),
            'gender': forms.Select(attrs={'class': 'form-select form-control w-100'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Apenas números'}),
            'email': forms.EmailInput(attrs={'class': 'form-control w-100'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'phone': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': '(DD)999999999'}),
            'specialties': Select2MultipleWidget(attrs={'class': 'w-100'}),
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
            'specialties': 'Especialidades',
            'user': 'Usuário vinculado',
        }
        
