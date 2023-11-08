#aca arriba van los imports solos o los de django exclusivamente, luego de paquetes isntalados, por ejemplo los de jdango y despues los del proyecto
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth. decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from cuentas.forms import MiFormularioDeRegistro, MiFormularioDeEdicion
from cuentas.models import	DatosCuenta

def login(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)    
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            django_login(request, user)
            #la siguente linea se agrega despues, como datos extra del usuario
            DatosCuenta.objects.get_or_create(user=request.user)

            return redirect('inicio')
    return render(request, 'cuentas/login.html', {'formulario_de_login':formulario})

def registro(request):
    formulario = MiFormularioDeRegistro() #se crea el formulario 
    if request.method == 'POST': #si el formulario tiene datos
        formulario = MiFormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()#Es posible guardar el formulario poraque ya está relacionado con el modelo
            return redirect('login')
    return render(request, 'cuentas/registro.html', {'formulario_de_registro': formulario}) #si no tiene datos

@login_required
def perfil(request):
    datos_cuenta = request.user.datoscuenta
    usuario = request.user
    return render(request, 'cuentas/perfil.html', {'usuario':usuario, 'direccion':datos_cuenta.direccion})

@login_required
def editar_perfil(request):
    
    datos_cuenta = request.user.datoscuenta
    formulario = MiFormularioDeEdicion(initial={'direccion':datos_cuenta.direccion, 'avatar':datos_cuenta.avatar}, instance=request.user)
    
    if request.method == 'POST':
            formulario = MiFormularioDeEdicion(request.POST, request.FILES, instance=request.user)
            
            if formulario.is_valid():
                nueva_direccion = formulario.cleaned_data.get('direccion')
                nuevo_avatar = formulario.cleaned_data.get('avatar')

                if nueva_direccion:
                    datos_cuenta.direccion = nueva_direccion
                    
                if nuevo_avatar:
                    datos_cuenta.avatar = nuevo_avatar
                    
                datos_cuenta.save()
                formulario.save()
                return redirect('perfil')
            
    return render(request, 'cuentas/editar_perfil.html', {'formulario_de_edicion': formulario})

class CambioClave(PasswordChangeView):
    template_name = 'cuentas/editar_clave.html'
    success_url = reverse_lazy('perfil')