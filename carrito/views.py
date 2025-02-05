from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito, CarritoItem, Compra, ProductoCompra
from web_Nova.models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})

@login_required
def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    
    if request.method == "POST":
        action = request.POST.get('action')     
        if action == "incrementar":
            item.cantidad += 1
        elif action == "decrementar" and item.cantidad > 1:
            item.cantidad -= 1
        
        item.save()  

    if creado and request.method != "POST":
        item.cantidad = 1  
        item.save()
    
    return redirect('ver_carrito')

@login_required
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        carrito.items.all().delete()
    return redirect('ver_carrito')


#Def de Pagos

@login_required
def formulario_pago(request, carrito_id):
    # Obtén el carrito del usuario con el id proporcionado
    carrito = Carrito.objects.get(id=carrito_id, usuario=request.user)

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        metodo_pago = request.POST.get('metodo_pago')

        total_carrito = carrito.total()  # Calcular el total

        # Crear la compra
        compra = Compra.objects.create(
            usuario=request.user,
            direccion_envio=direccion,
            metodo_pago=metodo_pago,
            total=total_carrito
        )

        # Asociar los productos del carrito con la compra
        for item in carrito.items.all():
            ProductoCompra.objects.create(
                compra=compra,
                producto=item.producto,
                cantidad=item.cantidad,
                precio_unitario=item.producto.precio_producto
            )

        # Limpiar los productos del carrito
        carrito.items.set([])  # Eliminar todas las relaciones del carrito

        
        # carrito.total = 0  
        # carrito.save()  

        # Opcional: Mensaje de éxito para el usuario
        messages.success(request, "¡Compra realizada con éxito!")

        return redirect('compra_exitosa', compra_id=compra.id)

    return render(request, 'carrito/formulario_pago.html', {'carrito': carrito})


def compra_exitosa(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    print(compra.usuario)
    
    return render(request, 'carrito/compra_exitosa.html', {'compra': compra})

def historial_compras(request):
    compras = Compra.objects.filter(usuario=request.user).order_by('-fecha_compra')
    return render(request, 'carrito/historial_compras.html', {'compras': compras})