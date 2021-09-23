from django import forms
from django.db.models import fields
from .models import Viaje, Destino

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje

        fields = '__all__'

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        
        fields = '__all__'