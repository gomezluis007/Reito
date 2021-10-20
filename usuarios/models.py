from django.db import models
from django.contrib.auth.models import User
from reito import settings

# Create your models here.

# Modelo que representa a un usuario del sistema.
class Usuario(User):
    telefono= models.BigIntegerField()
    foto=models.FileField(default=None,upload_to="img/",blank=True,null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return self.get_full_name()