from django.db import models

# Create your models here.

Categoria_producto = (
    ('Jueguete', 'Jueguete'),
    ('Comida', 'Comida'),
    ('Collar', 'Collar'),
    ('Higiene', 'Higiene'),
    ('Accesorio', 'Accesorio'),
    ('Otro', 'Otro'),
)

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    precio = models.IntegerField(null=True,blank=True)
    marca = models.CharField(max_length=50, null=False)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    tipo_producto = models.CharField(max_length=20, choices=Categoria_producto, default='Sin categoria')

    def __str__(self):
        return self.nombre