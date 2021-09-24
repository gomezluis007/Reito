from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Viaje, Destino

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje

        fields = 'destino', 'fecha', 'hora', 'asientos', 'precio', 'descripcion'

        widgets = {
            'destino':forms.Select(attrs={'class':'form-control'})
        }

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        
        fields = '__all__'