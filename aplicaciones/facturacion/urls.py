from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # Tipos de Movimientos
    path('facturacion/tipos-movimientos-lista/', views.fac_tipos_movimientos_lista, name = 'tipos-mov-lista'),
    path('facturacion/tipos-movimientos-crear/', views.fac_tipos_movimientos_crear, name = 'tipos-mov-crear'),
    path('facturacion/tipos-movimientos-modificar/<cod_movimiento>', views.fac_tipos_movimientos_modificar, name = 'tipos-mov-modificar'),
    path('facturacion/tipos-movimientos-eliminar/<cod_movimiento>', views.fac_tipos_movimientos_eliminar, name = 'tipos-mov-eliminar'),
]
