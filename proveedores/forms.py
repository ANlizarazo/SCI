from django.forms import ModelForm
from proveedores.models import Proveedor

class ProveedorForm(ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedoreform."""

        model = Proveedor
        fields='__all__'

class ProveedorUpdateForm(ModelForm):
    class Meta:
        model= Proveedor
        fields='__all__'