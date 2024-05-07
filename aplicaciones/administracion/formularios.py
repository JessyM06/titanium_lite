from django import forms
from .models import adm_contactos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Para cambiar el orden y listar solo los campos que necesito se debe mandar la lista, asi:
# fields = ['nombre', 'correo', 'tipo_consulta', etc] - Se listan los campos que vamos a requerir

# Para modificar el widgets de un campo se puede hacer de la siguiente manera:
# 1. Agregando esta linea antes de la instruccion 'class Meta:'
#    mensaje = forms.CharField(widget=forms.TextInput)
# 2. Agregando estas líneas despues del detalle de 'fields'
#        widgets = { 
#            'mensaje': forms.TextInput 
#            'val_precio_venta': forms.DecimalField 
#            'fecha': forms.SelectDateWidget()
#        }

class ContactoForm(forms.ModelForm):
    class Meta:
        model = adm_contactos
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']