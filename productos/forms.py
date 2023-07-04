from django.forms import ModelForm
from productos.models import Producto
from django.forms import ValidationError

def clean_email(self):
    email = self.cleaned_data["email"]
    existe = Producto.objects.filter(email_iexact=email).exists()

    if existe:
        raise ValidationError ("ya existe este email")
    return email

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
