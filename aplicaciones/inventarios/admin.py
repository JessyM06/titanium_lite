from django.contrib import admin
from .formularios import ProductosForm

# Registramos nuestros modelos en el admin de django para poderlos administrar desde ahí
from .models import inv_lineas_productos, inv_unidades_medida, inv_catalogo_productos
from .models import inv_cajas, inv_tipos_movimientos

# Modifica la forma de ver la tabla en el admin de django
class inv_catalogo_productos_Admin(admin.ModelAdmin):
    list_display = ['nbr_producto', 'cod_unidad', 'cod_linea', 'val_costo_unitario', 'val_precio_venta', 'num_existencia_actual']
    list_editable = ['val_costo_unitario', 'val_precio_venta']
    search_fields = ['nbr_producto']
    list_filter = ['nbr_producto']
    list_per_page = 5
    form = ProductosForm

# Registramos nuestros modelos
admin.site.register(inv_lineas_productos)
admin.site.register(inv_unidades_medida)
admin.site.register(inv_catalogo_productos, inv_catalogo_productos_Admin)
admin.site.register(inv_cajas)
admin.site.register(inv_tipos_movimientos)
