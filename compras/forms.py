from django.forms import ModelForm
from compras.models import Compra

class CompraForm(ModelForm):
    """Form definition for Compra."""

    class Meta:
        """Meta definition for Compraform."""

        model = Compra
        fields = '_all_'

class CompraUpdateForm(ModelForm):
    class Meta:
        model= Compra
        exclude=['fecha']
