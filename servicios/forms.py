from servicios.models import Servicios


class ServicioForm(Forms.ModelForm):
    """Form definition for Clientes."""

    class Meta:
        """Meta definition for Clientesform."""

        model = Servicios
        fields = '__all__'