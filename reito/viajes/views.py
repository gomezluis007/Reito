from reito.viajes.models import Viaje, Destino
from django.shortcuts import render
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .forms import DestinoForm, ViajeForm

class NuevoViaje(CreateView):
    model = Viaje
    #extra_context = {'':''}
    form_class = ViajeForm
    success_url = reverse_lazy('viajes:detalle')

class NuevoDestino(CreateView):
    model = Destino
    #extra_context = {'':''}
    form_class = DestinoForm
    success_url = reverse_lazy('viajes:detalle_destino')

class DetalleViaje(DetailView):
    model = Viaje

class EditarViaje(UpdateView):
    model = Viaje
    form_class = ViajeForm
    #extra_context = {'':''}
    success_url = reverse_lazy('viajes:detalle')

class EliminarViaje(DeleteView):
    model = Viaje
    success_url = reverse_lazy('viajes:nuevo')