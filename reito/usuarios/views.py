from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from .models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your tests here.

class NuevoUsuario(CreateView):
    model=Usuario
    form_class=UsuarioForm
    template_name="signup.html"
    success_url=reverse_lazy("usuarios:login")

def ver_mi_usuario(request):
    user=request.user
    return redirect("usuarios:ver_usuario", pk=user.id)

class VerUsuario(DetailView):
    model=Usuario
    template_name="detalle.html"