from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Vehiculo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import Vehiculos_editar, VehiculosForm
from django.urls import reverse_lazy
from usuarios.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin

# This class is used to create a new vehicle and has the validation
# to check that the user is logged in first


class VehiculoCrear(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculosForm
    template_name = "nuevo_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

    # This method is used to obtain the id of the logged in user since
    # in the front end this id is required for the creation of a vehicle because
    # this id is a foreign key of the vehicle
    def form_valid(self, form):
        usuario = get_object_or_404(Usuario, id=self.request.user.id)
        form.instance.id_usuario = usuario
        return super().form_valid(form)

# This class has the function of allowing the modification of an existing vehicle
# taking as a form a special form which only requests the description since
# for security this is the only modifiable field.


class VehiculoActualizar(UpdateView):
    model = Vehiculo
    form_class = Vehiculos_editar
    template_name = "editar_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')


class VehiculoEliminar(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

# This class is in charge of displaying the information of a vehicle in case # a user wants to see their vehicle.


class VehiculoDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    form_class = VehiculosForm
    context_object_name = 'vehiculo'
    template_name = "detalle_vehiculo.html"
