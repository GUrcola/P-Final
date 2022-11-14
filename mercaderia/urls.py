from django.urls import path
from mercaderia import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('crear_producto/', views.crear_producto, name='crear_productos'),
    path('ver_producto/', views.ver_producto, name='ver_productos'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
]
