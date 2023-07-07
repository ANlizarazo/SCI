from django.forms import ModelForm
from compras.models import DetalleCompra

class DetalleCompraForm(ModelForm):
    """Form definition for Compra."""

    class Meta:
        """Meta definition for Compraform."""

        model = DetalleCompra
        exclude=['estado']

class CompraUpdateForm(ModelForm):
    class Meta:
        model= DetalleCompra
        exclude=['proveedor, producto']
