from django.apps import AppConfig


class ProfessionalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.professional'

    def ready(self):
        import apps.professional.signals