from django.forms import ModelForm
from servicios.models import Servicio,TipoServicio

class ServicioForm(ModelForm):
    """Form definition for Servicio."""

    class Meta:
        """Meta definition for Servicioform."""

        model = Servicio
        fields = '__all__'

class TipoServicioForm(ModelForm):
    """Form definition for Servicio."""

    class Meta:
        """Meta definition for Servicioform."""

        model = TipoServicio
        exclude=['estado']

class ServicioUpdateForm(ModelForm):
    class Meta:
        model= Servicio
        fields = '__all__'
