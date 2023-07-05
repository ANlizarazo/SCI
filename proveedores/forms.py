from django.forms import ModelForm
from proveedores.models import Proveedor

class ProveedorForm(ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedorform."""

        model = Proveedor
        exclude=['estado']

class ProveedorUpdateForm(ModelForm):
    class Meta:
        model= Proveedor
        exclude=['numDocumento']