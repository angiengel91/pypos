from django.db import models
from bases.models import ClaseModelo

# NOTA:
# El campo Id lo crea DJango de forma automática, incremental, identity, primary key

#Clase Categoría
class Categoria(ClaseModelo):
    Descripcion =  models.CharField(
        max_length = 100,
        help_text = 'Descripción de la categoría', #Funciona como un tooltip o un placeholder, texto que se muestra en las cajas de tipo input
        unique = True #Valores únicos
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

#Clase Sub Categoría
class Subcategoria(ClaseModelo):
    objCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Descripcion =  models.CharField(
        max_length = 100,
        help_text = 'Descripción de la subcategoría',
    )

    #mostrar el nombre de la clase de la manera--> Categoría:Subcategoria
    def __str__(self):
        return '{}:{}'.format(self.objCategoria.Descripcion, self.Descripcion)
    
    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(Subcategoria, self).save()
    
    class Meta:
        verbose_name_plural = 'Subcategorias'
        unique_together = ('objCategoria', 'Descripcion') #Valores únicos por categoría


#Clase Marca
class Marca(ClaseModelo):
    Descripcion =  models.CharField(
        max_length = 100,
        help_text = 'Descripción de la marca', #Funciona como un tooltip o un placeholder, texto que se muestra en las cajas de tipo input
        unique = True #Valores únicos
    )
    
    #Cuando se haga referencia al modelo, se a a mostrar uno o varios campos de la clase
    def __str__(self):
        return '{}'.format(self.Descripcion)

    #Sobreescribir el método SAVE de la clase padre, para que las descripciones se guarden en mayúsculas
    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(Marca, self).save()

    #Nombre de la clase en plural
    class Meta:
        verbose_name_plural = 'Marcas'

#Clase Unidades de Medida
class UM(ClaseModelo):
    Descripcion =  models.CharField(
        max_length = 100,
        help_text = 'Descripción de la UM', #Funciona como un tooltip o un placeholder, texto que se muestra en las cajas de tipo input
        unique = True #Valores únicos
    )
    
    def __str__(self):
        return '{}'.format(self.Descripcion)

    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(UM, self).save()

    class Meta:
        verbose_name_plural = 'Unidades de Medida'

#Clase Productos
class Producto(ClaseModelo):
    Codigo =  models.CharField(max_length = 20, unique = True)
    Codigo_Barra = models.CharField(max_length = 50)
    Descripcion = models.CharField(max_length = 200)
    Precio = models.FloatField(default=0)
    Existencia = models.IntegerField(default=0)    
    Ultima_Compra = models.DateField(null=True, blank=True)
    objMarca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    objUM = models.ForeignKey(UM, on_delete=models.CASCADE)
    objSubcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.Descripcion)

    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = 'Unidades de Medida'
        unique_together = ('Codigo', 'Codigo_Barra')