from django.urls import path
from mercaderia import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('ver_producto/', views.ver_producto, name='ver_productos'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('eliminar/<int:id>', views.eliminarM, name='eliminarM'),
    path('ver_prod/<int:pk>', views.ver_prod.as_view(), name='ver_producto'),
    path('editar_prod/<int:pk>', views.editar_prod.as_view(), name='editar_prod')
]
