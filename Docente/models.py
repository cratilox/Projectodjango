from django.db import models

# Create your models here.
Eleccion_raza = (
    ('Desconocido', 'Desconocido'),
    ('Mestizo', 'Mestizo'),
    ('Raza_registrada', 'Raza registrada'),
)

class Docente (models.Model):
    fotografia = models.ImageField(upload_to='docentes')
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    grado_academico = models.CharField(max_length=20, choices=Eleccion_raza)

    def __str__(self):
        return str(self.fotografia)


