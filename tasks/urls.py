# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('login/', views.login, name='login'),  # URL para la vista de inicio de sesión
    path('getproveedores/', views.get_proveedores_list, name='get_proveedores_list'),
    path('getproveedores/updateprov/<int:id_proveedor>/', views.updateprov, name='update_prov'),
    path('search/<str:search_query>/', views.get_proveedores_list, name='search_proveedores_list'),
    path('trafico-liquidacion/', views.traficoLiquidacionMod, name='trafico_liquidacion'),
    path('editar_fecha_liquidacion/<int:no_liquidacion>/<str:id_area>/', views.editarFechaLiquidacion, name='editar_fecha_liquidacion'),
    path('trafico-liquidacion/<str:no_liquidacion>/<str:id_area>/', views.traficoLiquidacionMod, name='trafico_liquidacion_search'),
]
