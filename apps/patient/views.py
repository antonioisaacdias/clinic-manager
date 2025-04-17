from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .models import ModelPacient
from .forms import PacientForm

class PatientCreateView(CreateView):
    model = ModelPacient
    form_class = PacientForm
    template_name = 'patient/pacient_form.html'
    success_url = reverse_lazy('patient_create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Cadastro de Paciente',
            'resume': 'Preencha os dados do paciente para registrá-lo no sistema.'
        }
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Paciente cadastrado com sucesso!")
        return response