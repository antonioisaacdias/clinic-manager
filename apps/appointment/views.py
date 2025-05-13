from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta, time
from django.utils.timezone import localtime, now
from .models import ModelSchedule, ModelAppointment, ModelSchedule
from apps.professional.models import ModelProfessional, ModelSpecialty
from .form import ModelAppointmentForm
from django.views.generic import ListView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy


def professional_schedule_list(request):
    professionals = ModelProfessional.objects.filter(is_active=True).order_by('name')
    
    info = {
            'title': 'Lista de agendas',
            'resume': 'Essa lista contém todas as agendas.'
        }
    
    return render(request, 'schedule/schedule_list.html', {
        'professionals': professionals,
        'info': info,
    })
