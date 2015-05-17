from django import forms
from django.forms import ModelForm
from models import *

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        exclude = ("votos",)
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo'}),
            'contenido': forms.Textarea(attrs={'class':'form-control','placeholder':'Contenido'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
            'fecha_creado': forms.DateTimeInput({'class':'form-control','placeholder':'Fecha de creado'}),
            'usuario': forms.TextInput(attrs={'class':'form-control','placeholder':'usuario'})
        }

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario