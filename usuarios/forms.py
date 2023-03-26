from django.forms import ModelForm
from usuarios.models import Usuario
class UsuarioForm(ModelForm):
    """Form definition for Usuario."""
    class Meta:
        """Meta definition for Usuarioform."""

        model = Usuario
        fields = '__all__'      
class UsuarioUpdateForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['numDocumento', 'tipoDocumento']
