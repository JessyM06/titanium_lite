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

Opciones_Efecto = [
  ('+', 'Aumenta Saldo'),
  ('-', 'Disminuye Saldo'),
]

class fac_tipos_movimientos(models.Model):
    cod_movimiento = models.CharField('Código Movimiento', max_length=3, primary_key=True)
    nbr_movimiento = models.CharField('Nombre Movimiento', max_length=50)
    lsv_efecto = models.CharField('Efecto del Movimiento', max_length=1, choices=Opciones_Efecto, default='+')
    str_serie_doc = models.CharField('Serie del Documento', max_length=12)
    num_correlativo_actual = models.BigIntegerField()

    class Meta:
        db_table = 'fac_tipos_movimientos'

    def __str__(self):
        return self.nbr_movimiento
