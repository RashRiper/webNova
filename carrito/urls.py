from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),

    path('formulario_pago/<int:carrito_id>/', views.formulario_pago, name='formulario_pago'),
    path('compra_exitosa/<int:compra_id>/', views.compra_exitosa, name='compra_exitosa'),

    path('historial_compras/', views.historial_compras, name='historial_compras'),
]
