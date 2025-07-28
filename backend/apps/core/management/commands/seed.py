from django.core.management.base import BaseCommand
from apps.professional.models import Specialty, Professional
from django.core.management import call_command
from faker import Faker
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    call_command('flush', interactive=False)



    def handle(self, *args, **kwargs):
        User = get_user_model()
        admin = User.objects.create_superuser(
            username='Antonio',
            email='antonioisaacvd@gmail.com',
            password='33202121'
        )

        self.stdout.write(self.style.SUCCESS(f'Dados para Login -> E-mail: {admin.email} | Senha: {admin.password}'))
        faker = Faker('pt_BR')

        specialties = [
            "Neuropediatria",
            "Psicologia",
            "Fonoaudiologia",
            "Terapia Ocupacional",
            "Fisioterapia",
            "Psicopedagogia",
            "Nutrição",
            "Musicoterapia",
            "Arteterapia",
            "Neuropsicologia",
            "Psiquiatria Infantil",
            "Serviço Social",
            "Terapia ABA"
        ]

        for specialty in specialties:
            Specialty.objects.get_or_create(name=specialty)
        self.stdout.write(self.style.SUCCESS('Especialidades criadas com sucesso!'))

        professionals = []
        for _ in range(25):
            professional, _ = Professional.objects.get_or_create(
                name=faker.name(),
                email=faker.email(),
                phone=faker.phone_number(),
                address=faker.address(),
                gender=faker.random_element(elements=('M', 'F')),
                birth_date=faker.date_of_birth(minimum_age=25, maximum_age=60),
                cpf=faker.unique.random_int(min=10000000000, max=99999999999),
                rg=faker.unique.random_int(min=10000000, max=99999999),
            )
            professionals.append(professional)

        self.stdout.write(self.style.SUCCESS('Profissionais criados com sucesso!'))

        specialties = Specialty.objects.all()
        for professional in professionals:
            professional.add_specialty(specialties.order_by('?').first())