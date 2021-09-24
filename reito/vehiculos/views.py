from django.shortcuts import get_object_or_404, render
from .models import Vehiculo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import VehiculosForm
from django.urls import reverse_lazy
from usuarios.models import Usuario

class VehiculoCrear(CreateView):
    model = Vehiculo
    form_class = VehiculosForm
    template_name = "nuevo_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

    def form_valid(self, form):
        usuario = get_object_or_404(Usuario, id=self.request.user.id)
        form.instance.id_usuario = usuario
        return super().form_valid(form)

class VehiculoActualizar(UpdateView):
    model = Vehiculo
    fields = '__all__'
    success_url = reverse_lazy('ususrios:ver_mi_cuenta')

class VehiculoEliminar(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('ususrios:ver_mi_cuenta')

class VehiculoDetalle(DeleteView):
    model = Vehiculo

