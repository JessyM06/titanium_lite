from django import forms
from .models import fac_tipos_movimientos

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

class TiposMovForm(forms.ModelForm):
    class Meta:
        model = fac_tipos_movimientos
        fields = '__all__'
