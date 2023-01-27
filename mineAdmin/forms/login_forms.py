from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    pwd = forms.CharField(min_length=5, max_length=32)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(min_length=3, max_length=10)
    pwd = forms.CharField(min_length=5, max_length=32)
