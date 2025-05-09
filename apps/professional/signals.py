from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.professional.models import ModelProfessional
from apps.appointment.models import ModelSchedule
from datetime import date

@receiver(post_save, sender=ModelProfessional)
def create_schedule_for_professional(sender, instance, created, **kwargs):
    if created:
        schedule = ModelSchedule.objects.create(professional=instance)
        schedule.generate_day_slots(date.today())
        print(f'Agenda criada: {schedule}')