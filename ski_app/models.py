from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TipoUsuario(models.Model):
	tipo_user = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.tipo_user
    
class Usuario(AbstractUser):
	id_tipo_user = models.ForeignKey('TipoUsuario',on_delete=models.CASCADE,null=True, default='cliente',blank=True)
    

# equipos, categorias , estados 

class Estado(models.Model):
	nombre = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.nombre 
	
class Categoria(models.Model):
	nombre = models.CharField(max_length=50, unique=True)

class Equipo(models.Model):
	codigo = models.CharField(max_length=20,unique=True)
	nombre = models.CharField(max_length=50)
	
    