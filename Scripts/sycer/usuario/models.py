from django.db import models
from empresa import Empresa
# Create your models here.
class Usuario(models.Model):
	correo=models.EmailField(unique = True, null = False)
	clave=models.CharField(null = False)
	nombres=models.CharField(null = False, max_length=100)
	apellidos=models.CharField(null = False, max_length=100)
	telefono=models.CharField(null=True)
	foto= models.ImageField(upload_to='usuario')
	id_empresa = models.ForeignKey(Empresa)
	administrador = models.PositiveIntegerField(default = 0)