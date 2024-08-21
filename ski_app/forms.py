from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, TipoUsuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    id_tipo_user = forms.ModelChoiceField(queryset=TipoUsuario.objects.all(), required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'id_tipo_user']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        tipo= TipoUsuario.objects.filter(tipo_user='cliente').first()
        user.id_tipo_user = tipo
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        # Hacer que el campo 'id_tipo_user' sea oculto con HiddenInput
        self.fields['id_tipo_user'].required = False
        self.fields['id_tipo_user'].widget = forms.HiddenInput()