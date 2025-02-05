from django.db import models
from web_Nova.models import Producto
from django.contrib.auth.models import User

class Cotizacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cotización #{self.id} - ${self.total}"


class DetalleCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    nombre = models.CharField(max_length=100, default="No disponible")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"