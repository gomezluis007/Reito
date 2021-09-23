from django import forms
from django.db.models import fields
from .models import Viaje, Destino

class ViajeForm(forms.ModelForm):
    class Neta:
        model = Viaje

        fields = '__all__'

class DestinoForm(forms.ModelForm):
    class Neta:
        model = Destino

        fields = '__all__'