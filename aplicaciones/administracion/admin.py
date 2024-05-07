from django.contrib import admin

# Importamos nuestros modelos de la Aplicación Inventarios
from .models import adm_contactos

# Modifica la forma de ver la tabla en el admin de django
class adm_contactos_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'mensaje']
    search_fields = ['nombre', 'mensaje']
    list_filter = ['nombre', 'mensaje']

# Registramos nuestros modelos en el admin de django para poderlos administrar desde ahí
admin.site.register(adm_contactos, adm_contactos_Admin)
