from django import forms
from compras.models import Compra

class CompraForm(forms.ModelForm):
    """Form definition for Compra."""

    class Meta:
        """Meta definition for Compraform."""

        model = Compra
        fields = '__all__'
