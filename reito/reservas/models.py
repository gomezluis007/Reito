from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombre = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    viaje = models.ForeignKey("viajes.Viaje", verbose_name="Viaje", null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name='Pasajero', on_delete=models.CASCADE)
    estado = models.DateField(verbose_name="Estado", default=False)

    def __str__(self):
        return self.viaje + self.usuario
