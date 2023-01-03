from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    """Form definition for Usuarios."""

    class Meta:
        """Form definition for Usuariosform."""

        model = Usuario
        fields = '__all__'