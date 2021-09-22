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
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefono'})
        }

    def save(self, commit=True):
        user = super(UsuarioForm,self).save( commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user