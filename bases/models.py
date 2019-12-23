from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    #Fecha de Creación
    fc = models.DateTimeField(auto_now_add=True) #Esta fecha se agrega solamente 1 vez por el tipo de inicialización 
    #Fecha de Modificación
    fm = models.DateTimeField(auto_now=True) #Esta fecha se va a modificar en cada acción
    #Usuario que crea
    uc = models.ForeignKey(User, on_delete=models.CASCADE) #Esto especifica una relación directa con los usuarios que se crean en la sección admin del sitio
    #Usuario que modifica
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract=True #Esta sentencia hace que django omita este modelo en el momento de las migraciones