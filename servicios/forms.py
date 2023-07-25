from django.forms import ModelForm
from servicios.models import Servicio

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        exclude=['estado']

class ServicioUpdateForm(ModelForm):
    class Meta:
        model= Servicio
        exclude=['ciudad']
