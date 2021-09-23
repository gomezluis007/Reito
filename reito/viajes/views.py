from reito.viajes.models import Viaje
from django.shortcuts import render
from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .forms import ViajeForm

class NuevoViaje(CreateView):
    model = Viaje
    #extra_context = {'':''}
    form_class = ViajeForm
    success_url = reverse_lazy('viajes:detalle')
