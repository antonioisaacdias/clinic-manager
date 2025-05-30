from django.db import models
from uuid import uuid4
from apps.management.models import ModelPlan

# Create your models here.


class ModelPacient(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não informado'),
        ('O', 'Outro'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    plan = models.ForeignKey(ModelPlan, on_delete=models.CASCADE, null=True, blank=True)
    plan_card = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # criado automaticamente
    updated_at = models.DateTimeField(auto_now=True) 
    
    def get_gender_display_label(self):
        return dict(self.GENDER_CHOICES).get(self.gender, 'Desconhecido')