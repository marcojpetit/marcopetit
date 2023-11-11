from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='emisor', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='destinatario', on_delete=models.CASCADE)
    contenido = RichTextField()
    fecha_creacion = models.DateField(auto_now_add=True)   
    
    def __str__(self):
        return f'De: {self.emisor} - {self.fecha_creacion}'