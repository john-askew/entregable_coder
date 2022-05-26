from xml.dom.minidom import CharacterData
from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido