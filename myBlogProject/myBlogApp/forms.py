from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.PasswordInput()

    class Meta:
        fields = ['username','password']
