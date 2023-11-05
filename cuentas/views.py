from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from cuentas.forms import MiFormularioDeRegistro

def login(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)    
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            django_login(request, user)
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