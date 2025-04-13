from django.shortcuts import render

# Create your views here.
def create_patient_view(request):
    if request.method == 'GET':
        return render(request, 'patient/create-patient.html', {
            'info': {
                'title': 'Cadastro de novo paciente:',
                'resume': 'Insira dos dados do novo paciente no formulário abaixo.',
            }
            })