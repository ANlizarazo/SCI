from django.forms import ModelForm
from ciudad.models import Ciudad

class CiudadForm(ModelForm):

    class Meta:

        model = Ciudad
        exclude= ['estado']