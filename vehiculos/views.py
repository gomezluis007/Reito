from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from .models import Vehiculo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import Vehiculos_editar, VehiculosForm
from django.urls import reverse_lazy
from usuarios.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin

#Esta clase sirve para crear un nuevo vehículo y tiene la validacion
# para comprobar que primeramente el usuario esta logueado
class VehiculoCrear(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculosForm
    template_name = "nuevo_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

    #Este metodo sirve para obtener el id del usuario logueado ya que 
    # en el front end se requiere dicho id para la creacion de un vehiculo pues
    # este id es una llave foeranea del vehiculo
    def form_valid(self, form):
        usuario = get_object_or_404(Usuario, id=self.request.user.id)
        form.instance.id_usuario = usuario
        return super().form_valid(form)
#Esta clase tiene como funcion permitir la modificación de un vehiculo existente
# tomando como form un form especial el cual solicita solamente la descripcion ya que
# por seguridad este es el unico campo modificable.
class VehiculoActualizar(UpdateView):
    model = Vehiculo
    form_class = Vehiculos_editar
    template_name = "editar_vehiculo.html"
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')

class VehiculoEliminar(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('usuarios:ver_mi_cuenta')
# Esta clas ees la encargad ade mostrar la informacion de un vehiculo en caso
# de que un usuario desee ver su vehiculo.
class VehiculoDetalle(LoginRequiredMixin, DetailView):
    model = Vehiculo
    form_class = VehiculosForm
    context_object_name = 'vehiculo'
    template_name = "detalle_vehiculo.html"

    

    

    

    

