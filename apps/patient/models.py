from django.db import models
from uuid import uuid4

# Create your models here.


class ModelPacient(models.Model):
    
    class Gender(models.TextChoices):
        MALE = 'M', 'Masculino'
        FEMALE = 'F', 'Feminino'
        OTHER = 'O', 'Outro'
        NOT_INFORMED = 'N', 'Prefere não informar'
    
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100, blank=False, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.NOT_INFORMED)
    plan_card = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)