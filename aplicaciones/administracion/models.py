from typing import Any, Dict, Tuple
from django.db import models

# Atajos DJaneiro 
# mchar + tab   para columnas de tipo char
# fk + tab      para llaves foraneas
# mdecimal      para columnas de tipo decimal
# mint          para columnas enteras
# mimg          para columnas de imagen

# --------------------------------------------------------------------------------------------------------
# --- Creación de Modelos de Tablas de Nuestra Base de Datos
# --------------------------------------------------------------------------------------------------------

opciones_consultas = [
  (0, 'Consulta'),
  (1, 'Reclamo'),
  (2, 'Sugerencia'),
  (3, 'Comentario'),
]

class adm_contactos(models.Model):
    nombre = models.CharField('Nombre del Contacto', max_length=50)
    correo = models.EmailField('Correo Electrónico', max_length=254)
    tipo_consulta = models.IntegerField('Tipo Consulta', choices=opciones_consultas, default=0)
    mensaje = models.TextField('Mensaje Enviado')
    avisos = models.BooleanField('Recibir Notificaciones')

    class Meta:
        db_table = 'adm_contactos'

    def __str__(self):
        return self.nombre
