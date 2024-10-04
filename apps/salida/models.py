from django.db import models

# Create your models here.
class Salida(models.Model):
    categorias={
        ('metales','Metales'),
        ('plasticos','Plasticos'),
    }
    
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fechaSalida =models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre 