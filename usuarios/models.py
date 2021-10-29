from django.db import models
from django.contrib.auth.models import User
from reito import settings
from cloudinary.models import CloudinaryField


# Model representing a user of the system.
class Usuario(User):
    telefono = models.BigIntegerField()
    foto = CloudinaryField('image', default=None, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()
