from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class MiFormularioDeRegistro(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir clave', widget=forms.PasswordInput)
    
    class Meta:
        model = User #esto usa el modelo directamente y nos sirve para indicarle que campos del modelo queremos cargar. En este caso usamos uno de django pero puede ser por ejemplo para cursos
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
class MiFormularioDeEdicion(UserChangeForm):
    email = forms.EmailField(label='Email', required=False)
    password = None
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    direccion = forms.CharField(max_length=100, label='Dirección', required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User 
        fields = ['email', 'first_name', 'last_name', 'direccion', 'avatar']