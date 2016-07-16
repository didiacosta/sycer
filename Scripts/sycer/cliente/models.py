from django.db import models

# Create your models here.
class Cliente (models.Model):
	nit=models.CharField(max_length=30)
	nombre = models.CharField(max_length=50)
	estado = models.PositiveIntegerField()

	def __unicode__(self):
		return self.nombre
