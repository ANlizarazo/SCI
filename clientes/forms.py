from django.forms import ModelForm
from clientes.models import Cliente

class ClienteForm(ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = '__all__'

class ClienteUpdateForm(ModelForm):
    class Meta:
        model= Cliente
        exclude=['numDocumento']


