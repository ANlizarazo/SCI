
from proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
    """Form definition for Proveedore."""

    class Meta:
        """Meta definition for Proveedoreform."""

        model = Proveedor
        fields = '__all__'