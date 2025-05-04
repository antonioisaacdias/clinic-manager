from django.shortcuts import render
from .models import ModelPlan
from .forms import PlanForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

