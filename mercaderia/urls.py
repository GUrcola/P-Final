from django.urls import path
from mercaderia import views

urlpatterns = [
    path('', views.Inicio),
    path('crear_producto/<str:tipo>/<int:modelo>/', views.crear_producto),
    path('ver_producto/', views.ver_producto),
]
