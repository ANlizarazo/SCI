from django.forms import ModelForm
from ventas.models import Venta

class VentaForm(ModelForm):
    """Form definition for Venta."""

    class Meta:
        """Meta definition for Ventaform."""

        model = Venta
        fields = '__all__'

class VentaUpdateForm(ModelForm):
    class Meta:
        model= Venta
        exclude=['cliente','usuario']