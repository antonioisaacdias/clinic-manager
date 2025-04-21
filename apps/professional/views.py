from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ModelSpecialty, ModelProfessional
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import SpecialtyForm, ProfessionalForm
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

    
        situacao = self.request.GET.get('is_active')
        if situacao == 'True':
            queryset = queryset.filter(is_active=True)
        elif situacao == 'False':
            queryset = queryset.filter(is_active=False)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Lista de especialidade',
            'resume': 'Essa lista contém todos as expecialidades cadastradas.'
        }
        context['search_query'] = self.request.GET.get('q', '')
        context['is_active'] = self.request.GET.get('is_active', '')
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

class specialtyDeleteView(DeleteView):
    model = ModelSpecialty
    template_name = 'material-ui/partials/specialty-modal-delete.html'
    context_object_name = 'specialty'
    
    def get_success_url(self):
        messages.success(self.request, "Especialidade excluída com sucesso!")
        return reverse_lazy('specialty_list')

def change_specialty_activity_view(request, pk):
    specialty = get_object_or_404(ModelSpecialty, id=pk)
    specialty.is_active = not specialty.is_active
    specialty.save()
    return HttpResponse(status=204) 

class ProfessionalListView(ListView):
    model = ModelProfessional
    template_name = 'professional/professional_list.html'
    context_object_name = 'professionals'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(Q(name__icontains=search))

    
        situacao = self.request.GET.get('is_active')
        if situacao == 'True':
            queryset = queryset.filter(is_active=True)
        elif situacao == 'False':
            queryset = queryset.filter(is_active=False)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Lista de profissionais',
            'resume': 'Essa lista contém todos os profissionais cadastrados.'
        }
        context['search_query'] = self.request.GET.get('q', '')
        context['is_active'] = self.request.GET.get('is_active', '')
        return context

class ProfessionalCreateView(CreateView):
    model = ModelProfessional
    form_class = ProfessionalForm
    template_name = 'professional/professional_form.html'
    success_url = reverse_lazy('professional_create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Cadastro de profissional',
            'resume': 'Preencha os dados do profissional para cadastra-lo.'
        }
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Profissional cadastrado com sucesso!")
        return response
    
class ProfessionalDetailView(DeleteView):
    model = ModelProfessional
    template_name = 'professional/professional_detail.html'
    context_object_name = 'professional'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Dados do profissional',
            'resume': 'Abaixo estão os dados registrados do profissional no banco de dados.'
        }
        return context

def change_professional_activity_view(request, pk):
    professional = get_object_or_404(ModelProfessional, id=pk)
    professional.is_active = not professional.is_active
    professional.save()
    return HttpResponse(status=204) 