from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .models import ModelPacient
from .forms import PacientForm

class PatientCreateView(CreateView):
    model = ModelPacient
    form_class = PacientForm
    template_name = 'patient/patient_form.html'
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
    
class PatientListView(ListView):
    model = ModelPacient
    template_name = 'patient/patient_list.html'
    context_object_name = 'patients'
    paginate_by = 10
    ordering = ['name']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Lista de pacientes',
            'resume': 'Essa lista contém todos os pacientes cadastrados.'
        }
        return context
    
class PatientUpdateView(UpdateView):
    model = ModelPacient
    form_class = PacientForm
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient_create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Edição de paciente',
            'resume': 'Altere os dados do paciente para edita-lo no sistema.'
        }
        return context