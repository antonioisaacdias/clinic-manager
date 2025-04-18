from django.shortcuts import render
from .models import ModelSpecialty, ModelProfessional
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import SpecialtyForm
from django.db.models import Q
from django.contrib import messages

class SpecialtyCreateView(CreateView):
    model = ModelSpecialty
    form_class = SpecialtyForm
    template_name = 'specialty/specialty_form.html'
    success_url = reverse_lazy('specialty_create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Cadastro de Especialidade',
            'resume': 'Preencha os dados da especialidade para registrá-la no sistema.'
        }
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Especialidade cadastrada com sucesso!")
        return response

class SpecialtyListView(ListView):
    model = ModelSpecialty
    template_name = 'specialty/specialty_list.html'
    context_object_name = 'specialties'
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
            'title': 'Lista de especialidade',
            'resume': 'Essa lista contém todos as expecialidades cadastradas.'
        }
        context['search_query'] = self.request.GET.get('q', '')
        return context

class SpecialtyDetailView(DetailView):
    model = ModelSpecialty
    template_name = 'specialty/specialty_detail.html'
    context_object_name = 'specialty'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Dados da especialidade',
            'resume': 'Abaixo estão os dados registrados da especialidade no banco de dados.'
        }
        return context

class SpecialtyUpdateView(UpdateView):
    model = ModelSpecialty
    form_class = SpecialtyForm
    template_name = 'specialty/specialty_form.html'

    
    def get_success_url(self):
        messages.success(self.request, "Especialidade editada com sucesso!")
        return reverse_lazy('specialty_detail', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Edição de especialidade',
            'resume': 'Altere os dados da especialidade para edita-la no sistema.'
        }
        return context
