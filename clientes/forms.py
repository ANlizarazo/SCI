from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    """Form definition for Clientes."""

    class Meta:
        """Meta definition for Clientesform."""

        model = Cliente
        fields = '__all__'
