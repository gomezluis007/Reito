from django.db import models
from django.contrib.auth.models import User
from reito import settings

# Create your models here.

class Usuario(User):
    telefono= models.BigIntegerField()
    foto=models.FileField(default=None,upload_to="img/",blank=True,null=True)

    def __str__(self):
        return self.get_full_name()