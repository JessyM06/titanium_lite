from .inventarios.models import inv_catalogo_productos, inv_lineas_productos, inv_unidades_medida
from rest_framework import serializers

# Con exclude = ['nombre_campo'] podemos excluir algunas columnas

class inv_lineas_productos_serializers(serializers.ModelSerializer):
    class Meta:
        model = inv_lineas_productos
        fields = '__all__'

class inv_catalogo_productos_serializer(serializers.ModelSerializer):

    nbr_linea = serializers.CharField(read_only = True, source = 'cod_linea.nbr_linea')
    nbr_unidad = serializers.CharField(read_only = True, source = 'cod_unidad.nbr_unidad')

    class Meta:
        model = inv_catalogo_productos
        fields = '__all__'

