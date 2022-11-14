from django.db import models

class proveedores(models.Model):
    razon_social=models.CharField( max_length=20)
    ubicacion=models.CharField( max_length=50)
    
    def __str__(self):
        return f'Razon Social es {self.razon_social}, ubicado en {self.ubicacion}'
    
