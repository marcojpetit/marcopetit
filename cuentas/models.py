from django.db import models
from django.contrib.auth.models import User

class DatosCuenta(models.Model):
   #models.ForeignKey esto se usa para relacionar un modelo con otro por medio de FK
   user = models.OneToOneField(User, on_delete=models.CASCADE) #cascada es que cuando se elimina el usuario, este también, luego está el SET.NULL que es cuadno se elimina el usuario, este se mantiene pero sin relacionarse con ningun usuario,  el PROTECT, si hay un usuario relacionado a este dato, no se puede eliminar hasta que no se elimine el dato primero 
   direccion = models.CharField(max_length=100)