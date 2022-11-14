from django.db import models

class producto(models.Model):
    tipo = models.CharField(max_length=30)
    modelo = models.IntegerField()
    
    def __str__(self):
        return f'El producto es {self.tipo}, modelo/caracteristica  ({self.modelo})'