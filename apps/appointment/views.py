from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta, time
from django.utils.timezone import localtime, now
from .models import ModelSchedule, ModelAppointment
from .form import ModelAppointmentForm
from django.views.generic import ListView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy


class ModelAppointmentListView(ListView):
    model = ModelAppointment
    template_name = 'appointment/appointment_list.html'
    context_object_name = 'appointments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hoje = now().date()
        inicio_semana = hoje - timedelta(days=hoje.weekday())  # segunda-feira
        dias = [inicio_semana + timedelta(days=i) for i in range(7)]

        horarios = []
        hora = time(8, 0)
        while hora < time(18, 0):
            horarios.append(hora.strftime('%H:%M'))
            dt = datetime.combine(datetime.today(), hora) + timedelta(minutes=45)
            hora = dt.time()

        # monta agenda como dict[date][hora] = appointment
        agenda = {}
        for dia in dias:
            agenda[dia] = {}
            for h in horarios:
                agenda[dia][h] = None

        # popular os slots já existentes
        agendamentos = ModelAppointment.objects.filter(
            datetime__date__range=(dias[0], dias[-1])
        ).select_related('pacient')

        for appt in agendamentos:
            data = localtime(appt.datetime).date()
            hora = localtime(appt.datetime).time().strftime('%H:%M')
            if data in agenda and hora in agenda[data]:
                agenda[data][hora] = appt

        context.update({
            'info': {
                'title': 'Agenda semanal',
                'resume': 'Grade semanal de horários.'
            },
            'dias': dias,
            'horarios': horarios,
            'agenda': agenda
        })
        return context
        
class ModelAppointmentUpdateView(UpdateView):

    model = ModelAppointment
    form_class = ModelAppointmentForm
    template_name = 'appointment/appointment_form.html'

    
    def get_success_url(self):
        messages.success(self.request, "Paciente editado com sucesso!")
        return reverse_lazy('patient_update', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = {
            'title': 'Edição agendamento',
            'resume': 'Altere os dados do agendamento para edita-lo no sistema.'
        }
        return context