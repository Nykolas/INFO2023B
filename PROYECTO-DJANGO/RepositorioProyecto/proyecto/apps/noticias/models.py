from django.db import models

# Create your models here.

class Noticia(models.Model):

	creado = models.DateTimeField(
		'creado',
		auto_now_add=True
	)
	modificado = models.DateTimeField(
		'modificado',
		auto_now=True
	)
	titulo = models.CharField(max_length = 250)
	contenido = models.TextField()


	def __str__(self):
		return self.titulo