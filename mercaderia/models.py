from django.db import models

class producto(models.Model):
    tipo = models.CharField(max_length=30)
    modelo = models.IntegerField()
    descripcion= models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f'El producto es {self.tipo}, modelo/caracteristica  ({self.modelo})'