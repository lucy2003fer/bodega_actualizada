from django.db import models

# Create your models here.
class Registro(models.Model):
    categorias={
        ('metales','Metales'),
        ('plasticos','Plasticos'),
    }
    
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fechaIngreso =models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre