# suiteadministrativa/urls.py

from django.contrib import admin
from django.urls import path, include
from tasks import views  # Importa las vistas de la aplicación 'tasks'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # URL para la vista de la página de inicio
    path('login/', views.login, name='login'),  # Incluir las URLs de la aplicación 'tasks' para '/login/'
    path('support/',views.support, name='support'),
]


