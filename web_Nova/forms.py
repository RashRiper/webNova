from django import forms
from . models import Usuario
from .models import Producto


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['primer_nombre', 'segundo_nombre', 'rut', 'email', 'birthdate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'campo-texto'})

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio_producto', 'marca_producto', 'imagen', 'descripcion']      