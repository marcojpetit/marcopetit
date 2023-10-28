from django.shortcuts import render

def home (request):
    return render(request, 'home/index.html', {})

def sobre_mi (request):
    return render(request, 'home/sobre_mi.html', {})

def podcast_punto_alternativo (request):
    return render(request, 'home/podcast_punto_alternativo.html', {})

def cv (request):
    return render(request, 'home/cv.html', {})

def contacto (request):
    return render(request, 'home/contacto.html', {})