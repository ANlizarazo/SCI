from django.forms import ModelForm
from tecnico.models import Tecnico

class TecnicoForm(ModelForm):
    """Form definition for Tecnicos."""

    class Meta:
        """Meta definition for Tecnicoform."""

        model = Tecnico
        exclude=['estado']