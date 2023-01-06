from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    """Form definition for Usuario."""

    class Meta:
        """Form definition for Usuarioform."""

        model = Usuario
        fields = '__all__'