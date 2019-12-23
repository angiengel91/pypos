from django import forms
from .models import Categoria

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