from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TipoUsuario(models.Model):
	tipo_user = models.CharField(max_length=50, unique=True)
	
    def __str__(self):
		return self.tipo_user
    
class Usuario(AbstractUser):
	id_tipo_user = models.ForeignKey('TipoUsuario',on_delete=models.CASCADE,null=True)
    