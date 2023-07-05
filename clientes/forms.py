from django.forms import ModelForm
from clientes.models import Cliente
from django.forms import ValidationError


class ClienteForm(ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente        
        exclude=['estado']

def clean_email(self):
    email = self.cleaned_data["email"]
    existe = Cliente.objects.filter(email_iexact=email).exists()

    if existe:
        raise ValidationError ("ya existe este email")
    return email

class ClienteUpdateForm(ModelForm):
    class Meta:
        model= Cliente
        exclude=['numDocumento']
