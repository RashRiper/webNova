from django.shortcuts import render, get_object_or_404, redirect
from .models import Cotizacion, DetalleCotizacion
from web_Nova.models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

from django.shortcuts import render
from .models import Producto

def sacar_cotización(request):
    if request.method == "POST":
        presupuesto = float(request.POST.get('presupuesto'))
        total = 0

        # Seleccionar productos por categoría
        productos = {
            'placamadre': Producto.objects.filter(categoria='placamadre', precio_producto__lte=presupuesto).order_by('-precio_producto').first(),
            'procesador': Producto.objects.filter(categoria='procesador', precio_producto__lte=presupuesto).order_by('-precio_producto').first(),
            'memoriaram': Producto.objects.filter(categoria='memoria_ram', precio_producto__lte=presupuesto).order_by('-precio_producto').first(),
            'almacenamiento': Producto.objects.filter(categoria='almacenamiento', precio_producto__lte=presupuesto).order_by('-precio_producto').first(),
            'fuente': Producto.objects.filter(categoria='fuentepoder', precio_producto__lte=presupuesto).order_by('-precio_producto').first(),
        }

        # Crear cotización y detalles
        with transaction.atomic():
            cotizacion = Cotizacion.objects.create(presupuesto=presupuesto, total=0)

            for categoria, producto in productos.items():
                if producto:
                    total += producto.precio_producto
                    DetalleCotizacion.objects.create(
                        cotizacion=cotizacion,
                        producto=producto,
                        categoria=categoria,
                        precio=producto.precio_producto,
                        nombre=producto.nombre_producto,
                    )
                else:
                    DetalleCotizacion.objects.create(
                        cotizacion=cotizacion,
                        producto=None,
                        categoria=categoria,
                        precio=0,
                        nombre="No disponible",
                    )
            
            # Actualizar el total de la cotización
            cotizacion.total = total
            cotizacion.save()

        return render(request, 'cotizacion/resultado_cotizacion.html', {
            'cotizacion': cotizacion,
            'total': cotizacion.total,
            'presupuesto': cotizacion.presupuesto,
        })

    return render(request, 'cotizacion/sacar_cotizacion.html')

def resultado_cotizacion(request):
    cotizacion_id = request.GET.get('cotizacion_id', None)

    # Obtener la cotización según el ID o la última creada
    cotizacion = Cotizacion.objects.prefetch_related('detalles').filter(id=cotizacion_id).first() if cotizacion_id else Cotizacion.objects.prefetch_related('detalles').last()

    if not cotizacion:
        return render(request, 'cotizacion/resultado_cotizacion.html', {
            'error': 'No se encontró la cotización solicitada.',
        })

    return render(request, 'cotizacion/resultado_cotizacion.html', {
        'cotizacion': cotizacion,
        'total': cotizacion.total,
        'presupuesto': cotizacion.presupuesto,
    })


def listar_cotizaciones(request):
    cotizaciones = Cotizacion.objects.prefetch_related('detalles').all()
    return render(request, 'cotizacion/listar_cotizaciones.html', {'cotizaciones': cotizaciones})
