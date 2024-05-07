from django.contrib import admin

# Importamos nuestros modelos de la Aplicación Inventarios
from .models import fac_tipos_movimientos

# Registramos nuestros modelos en el admin de django para poderlos administrar desde ahí
admin.site.register(fac_tipos_movimientos)
