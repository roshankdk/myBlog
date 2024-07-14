from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.PasswordInput()

    class Meta:
        fields = ['username','password']

# new-story form
class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title','body','image1')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'body':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'fileinputclass'}),
        }