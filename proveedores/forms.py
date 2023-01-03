
from proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
    """Form definition for Clientes."""

    class Meta:
        """Meta definition for Clientesform."""

        model = Proveedor
        fields = '__all__'