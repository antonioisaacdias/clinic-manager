from django import forms
from .models import ModelAppointment

class ModelAppointmentForm(forms.ModelForm):
    class Meta:
        model = ModelAppointment
        fields = ['pacient', 'specialty', 'datetime']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'pacient': forms.Select(attrs={'class': 'form-select'}),
            'specialty': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'pacient': 'Paciente',
            'specialty': 'Especialidade',
            'datetime': 'Data e Hora da Consulta',
        }