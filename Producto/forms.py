from logging import PlaceHolder
from django import forms
from .models import Producto, Categoria_producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'marca', 'fecha_vencimiento', 'tipo_producto']

        labels = {
            'nombre': 'Nombre',
            'precio': 'Edad (Dejar en blanco si es que no se conoce)',
            'marca': 'Domicilio en donde se vive la Producto',
            'fecha_vencimiento': 'Fecha de nacimiento (Dejar en blanco si es que no se conoce)',
            'tipo_producto': 'Categoria de producto',

        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'tipo_producto': forms.Select(choices="Eleccion_animal",attrs={'class': 'form-control'}),
        }