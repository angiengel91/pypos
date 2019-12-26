from django.db import models
from bases.models import ClaseModelo

class Proveedor(ClaseModelo):
    Descripcion = models.CharField(max_length=100, unique=True)
    Direccion = models.CharField(max_length=250,null=True, blank=True)
    Contacto = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10, null=True, blank=True)
    Email = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.Descripcion)

    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"


