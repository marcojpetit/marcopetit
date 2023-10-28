from django.urls import path
from home.views import home, sobre_mi, podcast_punto_alternativo, cv, contacto

urlpatterns = [
    path('', home, name='inicio'),
    path('sobre_mi', sobre_mi, name='sobre_mi'),
    path(' podcast_punto_alternativo',  podcast_punto_alternativo, name='podcast_punto_alternativo'),
    path('cv', cv, name='cv'),
    path('contacto', contacto, name='contacto'),
    ]

