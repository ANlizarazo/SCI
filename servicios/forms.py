from servicios.models import Servicio


class ServicioForm(Forms.ModelForm):
    """Form definition for Clientes."""

    class Meta:
        """Meta definition for Clientesform."""

        model = Servicio
        fields = '__all__'