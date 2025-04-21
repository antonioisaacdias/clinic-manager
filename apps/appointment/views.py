from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta

# Create your views here.
def today_appointments_view(request):
    info = {
        'title': 'Agendamentos',
        'resume': 'Aqui estão os agendamentos da semana.'
    }
    return render(request, 'appointment/appointment_today.html', {'info': info})

def calendar_events(request):
    # Data base para os eventos
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    weekday = base_date.weekday()  # 0 = segunda, 6 = domingo
    monday = base_date - timedelta(days=weekday)

    # Eventos mockados
    events = [
        {
            "title": "Consulta - Dr. João",
            "start": (monday + timedelta(days=0, hours=9)).isoformat(),  # Segunda 9h
            "end": (monday + timedelta(days=0, hours=10)).isoformat(),
            "color": "#0288d1",
        },
        {
            "title": "Psicóloga Ana - Sessão",
            "start": (monday + timedelta(days=1, hours=14)).isoformat(),  # Terça 14h
            "end": (monday + timedelta(days=1, hours=15)).isoformat(),
            "color": "#66bb6a",
        },
        {
            "title": "Fonoaudióloga Clara",
            "start": (monday + timedelta(days=2, hours=10)).isoformat(),  # Quarta 10h
            "end": (monday + timedelta(days=2, hours=11)).isoformat(),
            "color": "#fbc02d",
        },
        {
            "title": "Consulta Particular - Dr. Pedro",
            "start": (monday + timedelta(days=3, hours=16)).isoformat(),  # Quinta 16h
            "end": (monday + timedelta(days=3, hours=17)).isoformat(),
            "color": "#ef5350",
        },
        {
            "title": "Retorno - Dra. Bruna",
            "start": (monday + timedelta(days=4, hours=11)).isoformat(),  # Sexta 11h
            "end": (monday + timedelta(days=4, hours=12)).isoformat(),
            "color": "#ab47bc",
        },
    ]

    return JsonResponse(events, safe=False)