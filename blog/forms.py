from django import forms

class CrearCategoriaFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la categoría", max_length=30, widget=forms.TextInput(attrs={'class': "input__field cf-validate"}))