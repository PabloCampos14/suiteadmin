from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import verificar_credenciales  # Importa la función para verificar credenciales
from django.contrib.auth.decorators import login_required
import pyodbc
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import activate
from datetime import datetime


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if verificar_credenciales(username, password):
            # Credenciales válidas, redirigir a la página de inicio
            return HttpResponse("Inicio de sesión exitoso. Redirigiendo a la página de inicio...")
        else:
            # Credenciales inválidas, mostrar mensaje de error
            error_message= "Credenciales inválidas. Por favor inténtelo de nuevo."
            return render(request, 'login.html', {'error': error_message})
    else:
        # Si no es una solicitud POST, mostrar el formulario de inicio de sesión
        return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def support(request):
    return render(request, 'support.html')

