from typing import Any, Dict, Tuple
from django.db import models

# Atajos DJaneiro 
# mchar + tab   para columnas de tipo char
# fk + tab      para llaves foraneas
# mdecimal      para columnas de tipo decimal
# mint          para columnas enteras
# mimg          para columnas de imagen
#
# def __str_(self) define el nombre del campo que mas representa al registro

# --------------------------------------------------------------------------------------------------------
# --- Creación de Modelos de Tablas de Nuestra Base de Datos
# --------------------------------------------------------------------------------------------------------

class inv_lineas_productos(models.Model):
    cod_linea = models.CharField('Código Línea', max_length=3, primary_key=True)
    nbr_linea = models.CharField('Nombre Línea', max_length=50)

    class Meta:
        db_table = 'inv_lineas_productos'

    def __str__(self):
        return self.nbr_linea

class inv_unidades_medida(models.Model):
    cod_unidad = models.CharField('Código Unidad', max_length=3, primary_key=True)
    nbr_unidad = models.CharField('Nombre Unidad', max_length=30)

    class Meta:
        db_table = 'inv_unidades_medida'

    def __str__(self):
        return self.nbr_unidad

class inv_catalogo_productos(models.Model):
    cod_producto = models.CharField('Código Producto', max_length=20, primary_key=True)
    nbr_producto = models.CharField('Nombre Producto', max_length=60)
    cod_linea = models.ForeignKey(inv_lineas_productos, on_delete=models.PROTECT, verbose_name='Línea de Producto') 
    cod_unidad = models.ForeignKey(inv_unidades_medida, on_delete=models.PROTECT, verbose_name='Unidad de Medida')
    cod_barra = models.CharField('Código de Barra', max_length=30)
    str_imagen = models.ImageField('Imagen', upload_to='imagenes/', null=True)
    val_costo_unitario = models.DecimalField('Costo Unitario', max_digits=9, decimal_places=2)
    val_precio_venta = models.DecimalField('Precio de Venta', max_digits=9, decimal_places=2)
    num_existencia_actual = models.IntegerField('Existencia Actual')

    class Meta:
        db_table = 'inv_catalogo_productos'

    def __str__(self):
        return self.nbr_producto
    
    def delete(self, using=None, keep_parents=False):

        if self.str_imagen:
            self.str_imagen.storage.delete(self.str_imagen.name)
        
        super().delete()

class inv_cajas(models.Model):
    cod_caja = models.CharField('Código Caja', max_length=3, primary_key=True)
    nbr_caja = models.CharField('Nombre Caja', max_length=50)

    class Meta:
        db_table = 'inv_cajas'

class inv_tipos_movimientos(models.Model):
    cod_tipo_mov = models.CharField('Código Tipo Movimiento', max_length=3, primary_key=True)
    nbr_tipo_mov = models.CharField('Nombre Tipo Movimiento', max_length=50)
    lsv_efecto = models.CharField('Efecto del Movimiento', max_length=1)

    class Meta:
        db_table = 'inv_tipos_movimientos'

#class inv_correlativos_mov(models.Model):
#    cod_tipo_mov = models.ForeignKey(inv_tipos_movimientos, on_delete=models.RESTRICT, unique=True)
#    cod_caja = models.ForeignKey(inv_cajas, on_delete=models.RESTRICT, unique=True)
#    cod_serie_doc = models.CharField('Serie del Documento', max_length=20)
#    num_correlativo_doc = models.BigIntegerField('Correlativo Documento')
#    class Meta:
#        db_table = 'inv_correlativos_mov'
