
from vehiculos.models import Vehiculo
from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from .models import Usuario
from .forms import EditarUsuarioForm, UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

# Create your tests here.

class NuevoUsuario(CreateView):
    model=Usuario
    form_class=UsuarioForm
    template_name="signup.html"
    success_url=reverse_lazy("usuarios:login")
    
# Login,Signup y Logout
class LoginUsuario(LoginView):
    model=Usuario
    template_name= 'login.html'

class LogoutUsuario(LogoutView):
    pass

@login_required
def ver_mi_usuario(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)
    vehiculo = Vehiculo.objects.filter(id_usuario=usuario).first()
    context={
        'usuario':usuario,
        'vehiculo':vehiculo
    }
    return render(request,"detalle_usuarios.html", context)

@login_required
def editar_mi_usuario(request):
    user=get_object_or_404(Usuario,id=request.user.id)
    if request.method == "POST":
        form=EditarUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("usuarios:ver_mi_cuenta")
    form=EditarUsuarioForm(instance=user)
    context={
        "form":form
    }
    return render(request,"editar_usuarios.html",context)

def ver_info_pasajero(request, pk):
    user = get_object_or_404(Usuario,id=pk)
    context= {
        'usuario':user
    }
    return render(request,'ver_info_pasajero.html',context)