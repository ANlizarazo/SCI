from django.forms import ModelForm
from tipodeservicio.models import TipoServicio

class TipoServicioForm(ModelForm):
    """Form definition for Servicio."""

    class Meta:
        """Meta definition for Servicioform."""

        model = TipoServicio
        exclude=['estado']