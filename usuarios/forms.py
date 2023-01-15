from django.forms import ModelForm
from usuarios.models import Usuario

class UsuarioForm(ModelForm):
    """Form definition for Usuario."""

    class Meta:
        """Meta definition for Usuarioform."""

        model = Usuario
        exclude=['estado']