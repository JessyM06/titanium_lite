from django import forms
from .models import inv_lineas_productos, inv_unidades_medida, inv_catalogo_productos
from .models import inv_cajas, inv_tipos_movimientos
from ..validators import Validador_MaxSizeFile
from django.forms import ValidationError


# Para cambiar el orden y listar solo los campos que necesito se debe mandar la lista, asi:
# fields = ['nombre', 'correo', 'tipo_consulta', etc] - Se listan los campos que vamos a requerir

# Para modifiicar el widgets de un campo se puede hacer de la siguiente manera:
# 1. Agregando esta linea antes de la instruccion 'class Meta:'
#    mensaje = forms.CharField(widget=forms.TextInput)
# 2. Agregando estas líneas despues del detalle de 'fields'
#        widgets = { 
#            'mensaje': forms.TextInput 
#            'val_precio_venta': forms.DecimalField 
#            'fecha': forms.SelectDateWidget()
#        }

class LineasForm(forms.ModelForm):
    class Meta:
        model = inv_lineas_productos
        fields = '__all__'

class UnidadesForm(forms.ModelForm):
    class Meta:
        model = inv_unidades_medida
        fields = '__all__'

class ProductosForm(forms.ModelForm):

    nbr_producto = forms.CharField(min_length=3, max_length=60)
    str_imagen = forms.ImageField(required=False, validators=[Validador_MaxSizeFile(max_file_size=1)])
    val_precio_venta = forms.DecimalField(min_value=1, max_value=25000)

    def clean_nbr_producto(self):
        nombre = self.cleaned_data['nbr_producto']
#        existe = inv_catalogo_productos.objects.filter(nbr_producto__iexact = nombre).exists()
#
#        if existe:
#            raise ValidationError('Nombre de Producto Ya Existe !!!')
        
        return nombre

    class Meta:
        model = inv_catalogo_productos
        fields = '__all__'

class CajasForm(forms.ModelForm):
    class Meta:
        model = inv_cajas
        fields = '__all__'

class TiposMovimientosForm(forms.ModelForm):
    class Meta:
        model = inv_tipos_movimientos
        fields = '__all__'