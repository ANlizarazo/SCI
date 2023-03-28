import contextvars
from django import forms
from usuarios.models import Usuario
from django.forms import ModelForm

class FormUsuario(forms.ModelForm):
    """Formulario de registro de un usuario en la base de datos
    
    Variables:

        - Password1: Contraseña
        - Password2: Verificación de la contraseña
    
    """

    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id' : 'password1',
            'required' : 'required',
        }
    ))

    password2 = forms.CharField(label = 'Verificación de la contrase', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id' : 'password1',
            'required' : 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username','nombres','apellidos','telefono','email','tipoDocumento','numDocumento','genero','rol')
        