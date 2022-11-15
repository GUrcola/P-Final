from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html') ,name='logout' ),
    path('crear/', views.crear, name='registar')
]
