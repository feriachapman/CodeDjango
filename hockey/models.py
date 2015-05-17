from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes',blank=True)
    fecha_creado = models.DateTimeField()
    votos = models.IntegerField(default=0)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    nick = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatar')
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    puntos = models.IntegerField(default=0)
    usuario = models.ForeignKey(User)
    articulo = models.ForeignKey(Articulo)

    def __unicode__(self):
        return self.nick