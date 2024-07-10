from django import forms
from .models import User

class UserForm(forms.Modelform):
    class Meta:
        model = User
        field = ['username','email','password']