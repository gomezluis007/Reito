from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Usuario
from reito.usuarios.forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your tests here.

class NuevoUsuario(CreateView):
    model=Usuario
    form_class=UsuarioForm
    template_name="signup.html"
    success_url=reverse_lazy("usuarios:login")
    
# Login,Signup y Logout
class LoginUsuario(LoginView):
    template_name= 'login.html'