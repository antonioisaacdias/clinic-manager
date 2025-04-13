from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='material-ui/home-base.html')),
    path('login/', TemplateView.as_view(template_name='material-ui/login.html'))
]