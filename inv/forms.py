from django import forms
from .models import CategoriaModelo, \
                    SubCategoriaModel

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaModelo
        fields=['descripcion','estado']
        labels = {'descripcion':'Descripcion de la categoría',
                  'estado':'Estado'}
        widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )


class SubCategoriaForm(forms.ModelForm):

    categoria = forms.ModelChoiceField(
        queryset=CategoriaModelo.objects.filter(estado=True).order_by('descripcion')
    )

    class Meta:
        model = SubCategoriaModel
        fields=['categoria', 'descripcion','estado']
        labels = {'descripcion':'Descripcion de la subcategoría',
                  'estado':'Estado'}
        widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )
        self.fields['categoria'].empty_label = "Seleccione Categoria"

