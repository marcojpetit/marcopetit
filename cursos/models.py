from django.db import models

class Curso(models.Model):
    mes = models.IntegerField()
    anio = models.IntegerField()
    nombre = models.CharField(max_length=70)
    instituto = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    horas = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.nombre} - {self.instituto}'