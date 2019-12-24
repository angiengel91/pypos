from django import forms
from .models import Categoria, Subcategoria, Marca, UM, Producto

# --------------------------------------------------------------- #
# --------------------- CATEGORIAS ------------------------------ #
# --------------------------------------------------------------- #

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Descripcion', 'estado']
        labels = {'Descripcion':'Descripción de la Categoría', 'estado':'Estado'}
        widget = {'Descripcion': forms.TextInput}

    #Este método está sobreescribiento el load del frm padre para que todos los elementos 
    # tomen la clase form-control de bootstrap y carguen con el css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

# ------------------------------------------------------------------ #
# --------------------- SUBCATEGORIAS ------------------------------ #
# ------------------------------------------------------------------ #

class SubcategoriaForm(forms.ModelForm):
    #Mostrar solo las categorías activas en los dropdown
    objCategoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('Descripcion')
    )
    class Meta:
        model = Subcategoria
        fields = ['objCategoria', 'Descripcion', 'estado']
        labels = {'Descripcion':'Subcategoría', 'estado':'Estado'}
        widget = {'Descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })        
        self.fields['objCategoria'].empty_label = 'Seleccione Categoría'

# ----------------------------------------------------------- #
# --------------------- MARCAS ------------------------------ #
# ----------------------------------------------------------- #

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['Descripcion', 'estado']
        labels = {'Descripcion':'Descripción de la Marca', 'estado':'Estado'}
        widget = {'Descripcion': forms.TextInput}

    #Este método está sobreescribiento el load del frm padre para que todos los elementos 
    # tomen la clase form-control de bootstrap y carguen con el css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

# ----------------------------------------------------------------------- #
# --------------------- UNIDADES DE MEDIDA ------------------------------ #
# ----------------------------------------------------------------------- #

class UMForm(forms.ModelForm):
    class Meta:
        model = UM
        fields = ['Descripcion', 'estado']
        labels = {'Descripcion':'Descripción de la Marca', 'estado':'Estado'}
        widget = {'Descripcion': forms.TextInput}

    #Este método está sobreescribiento el load del frm padre para que todos los elementos 
    # tomen la clase form-control de bootstrap y carguen con el css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

# ----------------------------------------------------------- #
# --------------------- PRODUCTOS --------------------------- #
# ----------------------------------------------------------- #

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Codigo', 'Codigo_Barra', 'Descripcion', 'estado', 'Precio', 'Existencia', 'Ultima_Compra', 'objMarca', 'objSubcategoria', 'objUM']
        exclude = ['um', 'fm', 'uc', 'fc']
        labels = {'Descripcion':'Descripción del Producto','Codigo_Barra':'Codigo de Barra', 'estado':'Estado', 'Ultima_Compra':'Fecha Ult. Compra'}
        widget = {'Descripcion': forms.TextInput}

    #Este método está sobreescribiento el load del frm padre para que todos los elementos 
    # tomen la clase form-control de bootstrap y carguen con el css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['Ultima_Compra'].widget.attrs['readonly'] = True
        self.fields['Existencia'].widget.attrs['readonly'] = True