from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import fac_tipos_movimientos

from .formularios import TiposMovForm

# Importamos la mensajería de DJango
from django.contrib import messages

# Importamos el Paginator desde django
from django.core.paginator import Paginator
from django.http import Http404

# Importamos el login_required para autorizacion de vistas
from django.contrib.auth.decorators import login_required, permission_required

# Creacion de Vistas

# -------------------------------------------------------------------------------------------
# --- Tipos de Movimientos
# -------------------------------------------------------------------------------------------

@permission_required('facturacion.view_inv_tipos_movimientos')
def fac_tipos_movimientos_lista (request):
    lista = fac_tipos_movimientos.objects.all().order_by('nbr_movimiento')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(lista, 6)
        lista = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': lista,
        'paginator': paginator
    }

    return render(request, 'facturacion/tipos-movimientos-lista.html', data)

@permission_required('facturacion.add_inv_tipos_movimientos')
def fac_tipos_movimientos_crear(request):
    form = TiposMovForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, 'Tipo de Movimiento Adicionado Correctamente !!!')
        return redirect('/facturacion/tipos-movimientos-lista/')
    return render(request, 'facturacion/tipos-movimientos-crear.html', {'formulario': form})

@permission_required('facturacion.change_inv_tipos_movimientos')
def fac_tipos_movimientos_modificar(request, cod_movimiento):
    TiposMov = get_object_or_404(fac_tipos_movimientos, cod_movimiento = cod_movimiento)
    form = TiposMovForm(request.POST or None, request.FILES or None, instance=TiposMov)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, f'Tipo de Movimiento { TiposMov.nbr_movimiento } Modificado Correctamente !!!')
        return redirect('/facturacion/tipos-movimientos-lista/')
    return render(request, 'facturacion/tipos-movimientos-modificar.html', {'formulario': form})

@permission_required('facturacion.delete_inv_tipos_movimientos')
def fac_tipos_movimientos_eliminar(request, cod_movimiento):
    TiposMov = get_object_or_404(fac_tipos_movimientos, cod_movimiento = cod_movimiento)
    TiposMov.delete()
    messages.success(request, f'Tipo de Movimiento { TiposMov.nbr_movimiento } Eliminado Correctamente !!!')
    return redirect('/facturacion/tipos-movimientos-lista/')
