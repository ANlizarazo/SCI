from django import forms
from ventas.models import Venta

class VentaForm(forms.ModelForm):
    """Form definition for Venta."""

    class Meta:
        """Form definition for Ventaform."""

        model = Venta
        fields = '__all__'