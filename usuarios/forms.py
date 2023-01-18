from tkinter import Widget
from django.forms import ModelForm, widgets
from usuarios.models import Usuario

class UsuarioForm(ModelForm):
    """Form definition for Usuario."""

    class Meta:
        """Meta definition for Usuarioform."""

        model = Usuario
        exclude=['estado']
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
    }        