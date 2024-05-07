from django.shortcuts import render, redirect

from .formularios import ContactoForm, CustomUserCreationForm

# Importamos la mensajería de DJango
from django.contrib import messages

# Importyamos estas dos funciones para autenticar usuarios manualmente
from django.contrib.auth import authenticate, login

# Creación de Vistas
def menu_principal (request):
    return render(request, 'administracion/menu_principal.html')

def contacto (request):
    form = ContactoForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, 'Mensaje Enviado Correctamente !!!')
        return redirect('/')
    return render(request, 'administracion/contacto.html', {'formulario': form})

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticamos el usuario
            user = authenticate(username = formulario.cleaned_data['username'], password = formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Registro Guardado Correctamente !!!')
            return redirect(to = '/')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)