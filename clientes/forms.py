from django.forms import ModelForm
from clientes.models import Cliente, Ciudad

class ClienteForm(ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = '__all__'

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'
