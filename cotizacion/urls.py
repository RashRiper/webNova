from django.urls import path
from .views import sacar_cotización, listar_cotizaciones, resultado_cotizacion

urlpatterns = [
    path('sacar-cotizacion/', sacar_cotización, name='sacar_cotizacion'),
    path('listar-cotizaciones/', listar_cotizaciones, name='listar_cotizaciones'),
    path('resultado-cotizacion/', resultado_cotizacion, name='resultado_cotizacion'),
]