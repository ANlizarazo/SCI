from clientes.models import Clientes

class ClientesForm(forms.ModelForm):
    """Form definition for Clientes."""

    class Meta:
        """Meta definition for Clientesform."""

        model = Clientes
        fields = ('__all__',)
