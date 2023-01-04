from servicios.models import Servicio


class ServicioForm(Forms.ModelForm):
    """Form definition for Servicio."""

    class Meta:
        """Meta definition for Servicioform."""

        model = Servicio
        fields = '__all__'