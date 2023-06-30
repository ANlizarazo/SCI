from django.forms import ModelForm
from departamentos.models import Departamento

class DepartamentoForm(ModelForm):

    class Meta:

        model = Departamento
        exclude= ['estado']
