from django.forms import ModelForm
from tecnicos.models import Tecnico

class TecnicoForm(ModelForm):
    """Form definition for Tecnico."""

    class Meta:
        """Meta definition for Tecnicoform."""

        model = Tecnico
        exclude=['estado']