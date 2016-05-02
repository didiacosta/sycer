from django.db import models

# Create your models here.
class Empresa(models.Model):
	nombre=models.CharField(max_length=255)
	nit=models.CharField(max_length=20)
	logo=models.ImageField(upload_to='empresa')
	estado=models.PositiveIntegerField(default=1)

