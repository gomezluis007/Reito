from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import Usuario
from viajes.models import Viaje
from .models import Reserva


def nueva_reserva(request, user_pk, viaje_pk):
    if(user_pk and viaje_pk):
        viaje = Viaje.objects.get(id=viaje_pk)
        usuario = Usuario.objects.get(id=user_pk)

        if(viaje.asientos > 0):
            reserva = Reserva.objects.create(viaje=viaje, usuario=usuario)
            reserva.save()
            messages.success(request, "Tu asiento ha sido reservado exitosamente")
            return redirect('viajes:index')
        else:
            messages.error(request, "Ya no hay asientos disponibles en este viaje")
            return redirect('viajes:index')
