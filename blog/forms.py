from django import forms
from ckeditor.fields import RichTextFormField

from .models import Categoria, Etiqueta

class CrearCategoriaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la categoría", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))

class CrearEtiquetaFormulario(forms.Form):
    nombre = forms.CharField(required=True, label="Nombre de la etiqueta", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))
    
class BaseEntradaFormulario(forms.Form):
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None, label="Por favor seleccione una categoría", widget=forms.Select(attrs={'class': "input__field cf-validate"}))
    titulo = forms.CharField(label="Título de la entrada", max_length=150, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))
    sub_titulo = forms.CharField(required=False, label="Subtítulo de la entrada", max_length=150, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))
    contenido = RichTextFormField(label="Escribir el contenido aquí", widget=forms.Textarea(attrs={'class': "input__field cf-validate"}))
    imagen_portada = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': "input__field cf-validate"}))
    etiquetas = forms.ModelMultipleChoiceField(queryset=Etiqueta.objects.all(), widget=forms.CheckboxSelectMultiple, required=False, label="Seleccione las etiquetas")
    
class CrearEntradaFormulario(BaseEntradaFormulario):
    ...
class ActualizarEntradaFormulario(BaseEntradaFormulario):
    ...
class ActualizarCategoriaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la categoría", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))

class ActualizarEtiquetaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la etiqueta", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))