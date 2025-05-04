from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.professional.models import ModelProfessional
from apps.appointment.models import ModelSchedule

@receiver(post_save, sender=ModelProfessional)
def create_schedule_for_professional(sender, instance, created, **kwargs):
    if created:
        ModelSchedule.objects.create(professional=instance)