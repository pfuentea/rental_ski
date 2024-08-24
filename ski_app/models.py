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
	def __str__(self):
		return self.nombre 

class Equipo(models.Model):
	codigo = models.CharField(max_length=20,unique=True)
	nombre = models.CharField(max_length=50)
	imagen = models.URLField(max_length=200, blank=True, null=True)
	categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='equipos' , default=5)
	estado = models.ForeignKey('Estado', on_delete=models.CASCADE, related_name='equipos',default=1)
	precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	def __str__(self):
		return self.nombre 
	
class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    fecha = models.DateTimeField()
    observacion = models.TextField(blank=True, null=True)


