from django.urls import path
from proveedores import views

urlpatterns = [
    path('proveedores/ver/',views.ver_proveedor, name='ver_proveedor'),
    path('proveedores/nuevo/',views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedores/eliminar/<int:id>', views.eliminar, name='eliminar')
]
