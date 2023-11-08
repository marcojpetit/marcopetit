from django.urls import path
from cuentas.views import login, registro, perfil, editar_perfil, CambioClave
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('editar_clave/', CambioClave.as_view(), name='editar_clave'),
]
