from django.forms import ModelForm
from proveedores.models import Proveedor

class ProveedorForm(ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedoreform."""

        model = Proveedor
        exclude=['estado']