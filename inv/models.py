from django.db import models
from bases.models import ClaseModelo

# NOTA:
# El campo Id lo crea DJango de forma automática, incremental, identity, primary key

#Clase Categoría
class Categoria(ClaseModelo):
    Descripcion =  models.CharField(
        max_length = 100,
        help_text = 'Descripción de la categoría', #Funciona como un tooltip o un placeholder, texto que se muestra en las cajas de tipo input
        unique = True
    )
    
    #Cuando se haga referencia al modelo, se a a mostrar uno o varios campos de la clase
    def __str__(self):
        return '{}'.format(self.Descripcion)

    #Sobreescribir el método SAVE de la clase padre, para que las descripciones se guarden en mayúsculas
    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(Categoria, self).save()

    #Nombre de la clase en plural
    class Meta:
        verbose_name_plural = 'Categorias'
