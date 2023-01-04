from ventas.models import Venta

class VentaForm(forms.ModelForm):
    """Form definition for ventas."""

    class Meta:
        """Form definition for Ventasform."""

        model = Venta
        fields = '__all__'