from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.user.urls')),
    path('api/v1/', include('apps.professional.urls')),
    path('api/v1/patients/', include('apps.patient.urls')),
]
