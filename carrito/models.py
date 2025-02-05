from django.db import models
from web_Nova.models import Producto
from django.contrib.auth.models import User

# Create your models here.

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    def total(self):
        return sum(item.subtotal() for item in self.items.all())
    

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre_producto}"

    def subtotal(self):
        return self.producto.precio_producto * self.cantidad
    

 #Compra Def

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=255)
    metodo_pago = models.CharField(max_length=100)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.usuario.username} - {self.fecha_compra}"


class ProductoCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='productos', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Cambiado de 'Producto' a Producto
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre_producto}"       