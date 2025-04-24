from django.db import models
from apps.professional.models import ModelProfessional, ModelSpecialty
from apps.patient.models import ModelPacient
from uuid import uuid4


class ModelSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    professional = models.OneToOneField(ModelProfessional, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Agenda de {self.professional.name}"

    
class ModelAppointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    schedule = models.ForeignKey(ModelSchedule,  on_delete=models.CASCADE)
    pacient = models.ForeignKey(ModelPacient, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    specialty = models.ForeignKey(ModelSpecialty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['schedule', 'datetime']

    def __str__(self):
        return f"{self.pacient.name} - {self.datetime.strftime('%d/%m/%Y %H:%M')}"