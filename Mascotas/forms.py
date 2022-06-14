from logging import PlaceHolder
from django import forms
from .models import Mascota

class mascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'edad', 'domicilio','fecha_nacimiento', 'raza']

        labels = {
            'nombre': 'Nombre',
            'edad': 'Edad -',
            'mensualidad': 'Mensualidad Pesos Chilenos',

        }
        PlaceHolder = {
            'nombre': 'Nombre',
            'edad': 'Dejar en blanco si no se conoce la edad'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'semestres': forms.TextInput(attrs={'class': 'form-control'}),
            'mensualidad': forms.TextInput(attrs={'class': 'form-control'}),
           
        }