from pickle import FALSE
from django.db import models

# Create your models here.

Eleccion_raza = (
    ('Desconocido', 'Desconocido'),
    ('Mestizo', 'Mestizo'),
    ('Raza_registrada', 'Raza registrada'),
)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=20, choices=Eleccion_raza)

    def __str__(self):
        return self.nombre