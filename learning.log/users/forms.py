from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = ('username', 'password1', 'password2')

def __innit__(self,*args, **kwargs):
    super().__innit__(*args,**kwargs)
    self.fields['username'].help_text = 'Usuario'
    self.fields['password1'].help_text = 'Senha'
    self.fields['password2'].help_text = 'Repita senha'