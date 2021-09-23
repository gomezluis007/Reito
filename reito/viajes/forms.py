from django import forms
from django.db.models import fields
from .models import Viaje

class ViajeForm(forms.ModelForm):
    class Neta:
        model = Viaje

        fields = '__all__'