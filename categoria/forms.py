from django.forms import ModelForm
from categoria.models import Categoria



class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        exclude=['estado']