from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Mensaje(models.Model):
    id_remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    #id_destinatario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = RichTextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return f'{self.id_remitente} para {self.id_remitente} - {self.fecha_creacion}'