from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, Mod


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', )


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ModForm(forms.ModelForm):
    class Meta:
        model = Mod
        fields = ['name', 'desc', 'url']
