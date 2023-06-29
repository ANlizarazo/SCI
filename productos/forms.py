from django.forms import ModelForm
from productos.models import Producto

class ProductoForm(ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Producto
        exclude=['estado']

class ProductoUpdateForm(ModelForm):
    class Meta:
        model= Producto
        exclude=['estado']
