from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .models import ModelPacient
from .forms import PacientForm
from django.db.models import Q

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
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(Q(name__icontains=search))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Lista de pacientes',
            'resume': 'Essa lista contém todos os pacientes cadastrados.'
        }
        context['search_query'] = self.request.GET.get('q', '')
        return context
    
class PatientUpdateView(UpdateView):
    model = ModelPacient
    form_class = PacientForm
    template_name = 'patient/patient_form.html'

    
    def get_success_url(self):
        messages.success(self.request, "Paciente editado com sucesso!")
        return reverse_lazy('patient_detail', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Edição de paciente',
            'resume': 'Altere os dados do paciente para edita-lo no sistema.'
        }
        return context
    
class PatientDetailView(DetailView):
    model = ModelPacient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Dados do paciente',
            'resume': 'Abaixo estão os dados registrados do paciente no banco de dados.'
        }
        return context
    
class PatientDeleteView(DeleteView):
    model = ModelPacient
    template_name = 'material-ui/partials/modal-delete.html'
    context_object_name = 'patient'
    
    def get_success_url(self):
        messages.success(self.request, "Paciente excluído com sucesso!")
        return reverse_lazy('patient_list')