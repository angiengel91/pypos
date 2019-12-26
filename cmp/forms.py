from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    Email = forms.EmailField(max_length=254)
    
    class Meta:
        model = Proveedor
        exclude = ['um','fm','uc','fc']
        widget={'Descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
