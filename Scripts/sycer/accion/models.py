from django.db import models

# Create your models here.
class Accion (models.Model):
	nombre=models.CharField(max_length=80)
