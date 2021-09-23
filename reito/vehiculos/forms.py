from django import forms
from .models import Vehiculo

class VehiculosForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields= '__all__'