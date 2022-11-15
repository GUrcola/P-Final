from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('usuario/login/', views.login, name='login'),
    path('usuario/logout/', LogoutView.as_view(template_name='usuario/logout.html') ,name='logout' )

]
