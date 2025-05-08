from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ModelPlan
from .forms import PlanForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages

class ModelPlanCreateView(CreateView):
    model = ModelPlan
    form_class = PlanForm
    template_name = 'plan/plan_form.html'
    success_url = reverse_lazy('plan_create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Cadastro de Plano',
            'resume': 'Preencha os dados do plano para registrá-lo no sistema.'
        }
        return context
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Plano cadastrado com sucesso!")
        return response

class ModelPlanListView(ListView):
    model = ModelPlan
    
    template_name = 'plan/plan_list.html'
    context_object_name = 'plans'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(Q(name__icontains=search))

    
        situacao = self.request.GET.get('is_active')
        if situacao == 'True' or situacao is None:
            queryset = queryset.filter(is_active=True)
        elif situacao == 'False':
            queryset = queryset.filter(is_active=False)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Lista de planos',
            'resume': 'Essa lista contém todos os convênios cadastrados.'
        }
        context['search_query'] = self.request.GET.get('q', '')
        context['is_active'] = self.request.GET.get('is_active', 'True')
        return context

class ModelPlanDetailView(DetailView):
    model = ModelPlan
    template_name = 'plan/plan_detail.html'
    context_object_name = 'plan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Dados do convênio',
            'resume': 'Abaixo estão os dados registrados do convênio no banco de dados.'
        }
        return context
    
def change_plan_activity_view(request, pk):
    plan = get_object_or_404(ModelPlan, pk=pk)
    plan.is_active = not plan.is_active
    plan.save()
    return HttpResponse(status=204) 

class ModelPlanDeleteView(DeleteView):
    model = ModelPlan
    template_name = 'material-ui/partials/plan-modal-delete.html'
    context_object_name = 'plan'
    
    def get_success_url(self):
        messages.success(self.request, "Plano excluído com sucesso!")
        return reverse_lazy('plan_list')
    
class ModelPlanUpdateView(UpdateView):

    model = ModelPlan
    form_class = PlanForm
    template_name = 'plan/plan_form.html'


    
    def get_success_url(self):
        messages.success(self.request, "Convênio editado com sucesso!")
        return reverse_lazy('plan_detail', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Edição plano',
            'resume': 'Altere os dados do convênio para edita-lo no sistema.'
        }
        return context