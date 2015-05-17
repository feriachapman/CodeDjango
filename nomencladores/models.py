from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.nombre