from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import inv_lineas_productos, inv_unidades_medida, inv_catalogo_productos
from .models import inv_cajas, inv_tipos_movimientos

from .formularios import LineasForm, UnidadesForm, ProductosForm

# Importamos la mensajería de DJango
from django.contrib import messages

# Importamos el Paginator desde django
from django.core.paginator import Paginator
from django.http import Http404

# Importamos el login_required para autorizacion de vistas
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework import viewsets
from ..serializers import inv_catalogo_productos_serializer, inv_lineas_productos_serializers

# Creacion de Vistas

# -------------------------------------------------------------------------------------------
# --- Líneas de Productos
# -------------------------------------------------------------------------------------------

@permission_required('inventarios.view_inv_lineas_productos')
def inv_lineas_productos_lista (request):
    lista = inv_lineas_productos.objects.all().order_by('nbr_linea')
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

    return render(request, 'inventarios/lineas-productos-lista.html', data)

@permission_required('inventarios.add_inv_lineas_productos')
def inv_lineas_productos_crear(request):
    form = LineasForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Línea de Producto Adicionada Correctamente !!!')
        return redirect('/inventarios/lineas-productos-lista/')
    return render(request, 'inventarios/lineas-productos-crear.html', {'formulario': form})

@permission_required('inventarios.change_inv_lineas_productos')
def inv_lineas_productos_modificar(request, cod_linea):
    Linea = get_object_or_404(inv_lineas_productos, cod_linea = cod_linea)
    form = LineasForm(request.POST or None, request.FILES or None, instance=Linea)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, f'Línea de Producto { Linea.nbr_linea } Modificada Correctamente !!!')
        return redirect('/inventarios/lineas-productos-lista/')
    return render(request, 'inventarios/lineas-productos-modificar.html', {'formulario': form})

@permission_required('inventarios.delete_inv_lineas_productos')
def inv_lineas_productos_eliminar(request, cod_linea):
    Linea = get_object_or_404(inv_lineas_productos, cod_linea = cod_linea)
    Linea.delete()
    messages.success(request, f'Línea de Producto { Linea.nbr_linea } Eliminada Correctamente !!!')
    return redirect('/inventarios/lineas-productos-lista/')


# -------------------------------------------------------------------------------------------
# --- Unidades de Medida
# -------------------------------------------------------------------------------------------

@permission_required('inventarios.view_inv_unidades_medida')
def inv_unidades_medida_lista (request):
    lista = inv_unidades_medida.objects.all().order_by('nbr_unidad')
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

    return render(request, 'inventarios/unidades-medida-lista.html', data)

@permission_required('inventarios.add_inv_unidades_medida')
def inv_unidades_medida_crear(request):
    form = UnidadesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Unidad de Medida Adicionada Correctamente !!!')
        return redirect('/inventarios/unidades-medida-lista/')
    return render(request, 'inventarios/unidades-medida-crear.html', {'formulario': form})

@permission_required('inventarios.change_inv_unidades_medida')
def inv_unidades_medida_modificar(request, cod_unidad):
    Unidad = get_object_or_404(inv_unidades_medida, cod_unidad = cod_unidad)
    form = UnidadesForm(request.POST or None, request.FILES or None, instance=Unidad)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, f'Unidad de Media { Unidad.nbr_unidad } Modificada Correctamente !!!')
        return redirect('/inventarios/unidades-medida-lista/')
    return render(request, 'inventarios/unidades-medida-modificar.html', {'formulario': form})

@permission_required('inventarios.delete_inv_unidades_medida')
def inv_unidades_medida_eliminar(request, cod_unidad):
    Unidad = get_object_or_404(inv_unidades_medida, cod_unidad = cod_unidad)
    Unidad.delete()
    messages.success(request, f'Unidad de Media { Unidad.nbr_unidad } Eliminada Correctamente !!!')
    return redirect('/inventarios/unidades-medida-lista/')


# -------------------------------------------------------------------------------------------
# --- Catalogo de Productos
# -------------------------------------------------------------------------------------------

@permission_required('inventarios.view_inv_catalogo_productos')
def inv_catalogo_productos_lista (request):
    lista = inv_catalogo_productos.objects.all().order_by('nbr_producto')
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

    return render(request, 'inventarios/catalogo-productos-lista.html', data)

@permission_required('inventarios.add_inv_catalogo_productos')
def inv_catalogo_productos_crear(request):
    form = ProductosForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Producto Adicionado Correctamente !!!')
        return redirect('/inventarios/catalogo-productos-lista/')
    return render(request, 'inventarios/catalogo-productos-crear.html', {'formulario': form})

@permission_required('inventarios.change_inv_catalogo_productos')
def inv_catalogo_productos_modificar(request, cod_producto):
    Producto = get_object_or_404(inv_catalogo_productos, cod_producto = cod_producto)
    form = ProductosForm(request.POST or None, request.FILES or None, instance=Producto)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, f'Producto { Producto.nbr_producto } Modificado Correctamente !!!')
        return redirect('/inventarios/catalogo-productos-lista/')
    return render(request, 'inventarios/catalogo-productos-modificar.html', {'formulario': form})

@permission_required('inventarios.delete_inv_catalogo_productos')
def inv_catalogo_productos_eliminar(request, cod_producto):
    Producto = get_object_or_404(inv_catalogo_productos, cod_producto = cod_producto)
    Producto.delete()
    messages.success(request, f'Producto { Producto.nbr_producto } Eliminado Correctamente !!!')
    return redirect('/inventarios/catalogo-productos-lista/')

# Creacion de clases para serializar / Entidades dentro de nuestra API
class inv_lineas_productos_viewset(viewsets.ModelViewSet):
    queryset = inv_lineas_productos.objects.all()
    serializer_class = inv_lineas_productos_serializers

class inv_catalogo_productos_viewset(viewsets.ModelViewSet):
    queryset = inv_catalogo_productos.objects.all()
    serializer_class = inv_catalogo_productos_serializer

    def get_queryset(self):
        productos = inv_catalogo_productos.objects.all()
        nbr_producto = self.request.GET.get('nbr_producto')

        if nbr_producto:
            productos = productos.filter(nbr_producto__contains = nbr_producto)

        return productos
