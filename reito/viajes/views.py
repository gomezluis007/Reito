from usuarios.models import Usuario
from .models import Viaje, Destino
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .forms import DestinoForm, ViajeForm

def index(request):
    return render(request, 'index.html')

class NuevoViaje(CreateView):
    model = Viaje
    #extra_context = {'':''}
    template_name="nuevo.html"
    form_class = ViajeForm
    success_url = reverse_lazy('viajes:index')

    def form_valid(self, form):
        usuario = get_object_or_404(Usuario, id=self.request.user.id)
        form.instance.conductor = usuario
        return super().form_valid(form)

class NuevoDestino(CreateView):
    model = Destino
    #extra_context = {'':''}
    form_class = DestinoForm
    success_url = reverse_lazy('viajes:detalle_destino')

def detalle_viaje(request, pk):
    viaje = get_object_or_404(Viaje, id=pk)
    context={
        'viaje':viaje
    }
    return render(request, "detalle_viaje.html", context)

class EditarViaje(UpdateView):
    model = Viaje
    form_class = ViajeForm
    #extra_context = {'':''}
    success_url = reverse_lazy('viajes:detalle')

class EliminarViaje(DeleteView):
    model = Viaje
    success_url = reverse_lazy('viajes:nuevo')

class DetalleViajeViajero(DetailView):
    model = Viaje
    template_name="detalle_viaje_viajero.html"

