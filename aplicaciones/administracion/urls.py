from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # Se deja el primer parametro en blanco para indicar que es el raiz del sitio y lo cargara de inicio
    path('', views.menu_principal, name = '/'),
    path('administracion/contacto/', views.contacto, name = 'contacto'),
    path('registro/', views.registro, name = 'registro'),
]
