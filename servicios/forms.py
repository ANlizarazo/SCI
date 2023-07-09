from django.forms import ModelForm
from servicios.models import Servicio

class ServicioForm(ModelForm):
    """Form definition for Servicio."""

    class Meta:
        """Meta definition for Servicioform."""

        model = Servicio
        exclude=['estado']


class ServicioUpdateForm(ModelForm):
    class Meta:
        model= Servicio
        exclude=['ciudad']
