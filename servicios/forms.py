from django import forms
from servicios.models import Servicio

class ServicioForm(forms.ModelForm):
    """Form definition for Servicio."""

    class Meta:
        """Meta definition for Servicioform."""

        model = Servicio
        fields = '__all__'