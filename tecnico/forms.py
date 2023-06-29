from django.forms import ModelForm
from tecnico.models import Tecnico

class TecnicoForm(ModelForm):
    """Form definition for Tecnico."""

    class Meta:
        """Meta definition for Tecnicoform."""

        model = Tecnico
        exclude=['estado','ciudad']

class TecnicoUpdateForm(ModelForm):
    #Formulario para modificar
    class Meta:
        model= Tecnico
        exclude=['numDocumento']