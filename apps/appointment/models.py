from django.db import models
from apps.professional.models import ModelProfessional, ModelSpecialty
from apps.patient.models import ModelPacient
from uuid import uuid4
from datetime import time, date, timedelta, datetime


class ModelSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    professional = models.OneToOneField(ModelProfessional, on_delete=models.CASCADE)
    slot_duration = models.IntegerField(default=45)
    active_days_of_week = models.CharField(max_length=7, default='0111110')
    time_start = models.TimeField(default=time(8, 0))
    time_end = models.TimeField(default=time(18, 0))
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    schedule_size = models.IntegerField(default=1)
    
    def __str__(self):
        days_name = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
        active_days = [days_name[i] for i, active in enumerate(self.active_days_of_week) if active == '1']
        days_str = ', '.join(active_days)

        hour_start = self.time_start.strftime('%H:%M') if hasattr(self.time_start, 'strftime') else str(self.time_start)
        hour_end = self.time_end.strftime('%H:%M') if hasattr(self.time_end, 'strftime') else str(self.time_end)

        return f"{self.professional.name} - {days_str} ({hour_start} - {hour_end})"

    
    def generate_day_slots(self, day):
        weekday = (day.weekday() + 1) % 7

        if self.active_days_of_week[weekday] == '1':
            start_time = time(hour=self.time_start.hour, minute=self.time_start.minute)
            current_dt = datetime.combine(day, start_time)

            slots = []
            while current_dt.time() < self.time_end:
                slots.append(current_dt)
                current_dt += timedelta(minutes=self.slot_duration)

            for slot in slots:
                ModelAppointment.objects.create(
                    schedule=self,
                    datetime=slot,
                )
                
    def generate_month_slots(self, dt):
        current_date = dt
        final_date = date(current_date.year, current_date.month + 1, 1) - timedelta(days=1)
        
        days = []
        
        while current_date <= final_date:
            days.append(current_date)
            current_date += timedelta(days=1)
            
        for day in days:
            self.generate_day_slots(day)
        
        
    
class ModelAppointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    schedule = models.ForeignKey(ModelSchedule,  on_delete=models.CASCADE)
    pacient = models.ForeignKey(ModelPacient, on_delete=models.CASCADE, blank=True, null=True)
    datetime = models.DateTimeField()
    specialty = models.ForeignKey(ModelSpecialty, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['schedule', 'datetime']

    def __str__(self):
        return f"{self.pacient.name} - {self.datetime.strftime('%d/%m/%Y %H:%M')}"
    