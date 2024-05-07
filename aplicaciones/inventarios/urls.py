from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('lineas_productos', views.inv_lineas_productos_viewset)
router.register('catalogo_productos', views.inv_catalogo_productos_viewset)

urlpatterns = [
    # Lineas de Productos
    path('inventarios/lineas-productos-lista/', views.inv_lineas_productos_lista, name = 'lineas-lista'),
    path('inventarios/lineas-productos-crear/', views.inv_lineas_productos_crear, name = 'lineas-crear'),
    path('inventarios/lineas-productos-modificar/<cod_linea>', views.inv_lineas_productos_modificar, name = 'lineas-modificar'),
    path('inventarios/lineas-productos-eliminar/<cod_linea>', views.inv_lineas_productos_eliminar, name = 'lineas-eliminar'),

    # Unidades de Medida
    path('inventarios/unidades-medida-lista/', views.inv_unidades_medida_lista, name = 'unidades-lista'),
    path('inventarios/unidades-medida-crear/', views.inv_unidades_medida_crear, name = 'unidades-crear'),
    path('inventarios/unidades-medida-modificar/<cod_unidad>', views.inv_unidades_medida_modificar, name = 'unidades-modificar'),
    path('inventarios/unidades-medida-eliminar/<cod_unidad>', views.inv_unidades_medida_eliminar, name = 'unidades-eliminar'),

    # Catálogo de Productos
    path('inventarios/catalogo-productos-lista/', views.inv_catalogo_productos_lista, name = 'productos-lista'),
    path('inventarios/catalogo-productos-crear/', views.inv_catalogo_productos_crear, name = 'productos-crear'),
    path('inventarios/catalogo-productos-modificar/<cod_producto>', views.inv_catalogo_productos_modificar, name = 'productos-modificar'),
    path('inventarios/catalogo-productos-eliminar/<cod_producto>', views.inv_catalogo_productos_eliminar, name = 'productos-eliminar'),

    path('api/', include(router.urls)),
]
