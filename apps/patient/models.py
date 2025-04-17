from django.db import models
from uuid import uuid4

# Create your models here.


class ModelPacient(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não informado'),
        ('O', 'Outro'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100, blank=False, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    plan_card = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    
    def get_gender_display_label(self):
        return dict(self.GENDER_CHOICES).get(self.gender, 'Desconhecido')