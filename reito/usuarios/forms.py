from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario

        fields='username','first_name','last_name','email','password','telefono'
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefono'})
        }
        labels = {
            'username': 'Nombre de usuario',
            'first_name': "Nombre(s)",
            'last_name': 'Apellidos',
            'email': 'Correo',
            'password':'Contraseña',
            'telefono':'Telefono'
        }
        help_texts = {
            'username': None,
        }

    def save(self, commit=True):
        user = super(UsuarioForm,self).save( commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=('username','first_name','last_name','email','telefono')

        labels = {
            'username': 'Nombre de usuario',
            'first_name': "Nombre(s)",
            'last_name': 'Apellidos',
            'email': 'Correo',
        }
