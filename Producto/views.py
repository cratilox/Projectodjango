from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Producto
from .forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/añadir_Productos.html'
    success_url = reverse_lazy('list_Producto')
    
class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/añadir_Productos.html'
    success_url = reverse_lazy('list_Producto')

class ProductoList(ListView):
    model = Producto
    template_name = 'core/listar_Productos.html'
    # paginate_by = 4

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'core/borrar_Producto.html'
    success_url = reverse_lazy('list_Producto')