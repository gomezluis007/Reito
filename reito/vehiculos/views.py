from django.shortcuts import render
from .models import Vehiculo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import VehiculosForm
from django.urls import reverse_lazy

class VehiculoCrear(CreateView):
    model = Vehiculo
    fields='__all__'
    template_name = "nuevo_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

class VehiculoActualizar(UpdateView):
    model = Vehiculo
    fields = '__all__'
    success_url = reverse_lazy('ususrios:ver_mi_cuenta')

class VehiculoEliminar(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('ususrios:ver_mi_cuenta')

class VehiculoDetalle(DeleteView):
    model = Vehiculo

