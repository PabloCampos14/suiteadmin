# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # URL para la vista de inicio de sesión
    # Otras URLs de la aplicación aquí...
]
