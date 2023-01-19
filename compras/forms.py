from django.forms import ModelForm
from compras.models import Compra

class CompraForm(ModelForm):
    """Form definition for Compra."""

    class Meta:
        """Meta definition for Compraform."""

        model = Compra
        fields = '__all__'
