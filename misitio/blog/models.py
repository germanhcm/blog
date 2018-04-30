from django.db import models
from django.utils import timezone

class Enviar(models.Model):
    autor = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    titulo = models.name = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
        default=timezone.now) 
    fecha_publicacion = models.DateTimeField(
        blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

