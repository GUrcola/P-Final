from django.db import models

class producto(models.Model):
    tipo = models.CharField(max_length=30)
    modelo = models.IntegerField()
    