from django import forms

class CrearCategoriaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la categoría", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))
class CrearEtiquetaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la etiqueta", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))
class CrearEntradaFormulario(forms.Form):
    titulo = forms.CharField(label="Título de la entrada", max_length=150, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))
    contenido = forms.CharField(label="Escribir el contenido aquí", widget=forms.Textarea(attrs={'class': "input__field cf-validate"}))
    imagen_portada = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': "input__field cf-validate"}))