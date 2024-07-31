from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Category, Comment

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
        fields = ('title','category','body','image1')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'category': forms.Select(attrs={'class': 'selectinputclass'}),         
            'body':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'fileinputclass'}),
        }

    
    def save(self, commit=True):
        new_category = self.cleaned_data.get('category')
        if new_category:
            category, created = Category.objects.get_or_create(name=new_category)
            self.instance.category = category
        return super().save(commit=commit)


# adding comment form 
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['author','body']

        widget = {
            'author': forms.TextInput(attrs={'class':'selectinputclass'}),
            'body': forms.Textarea(attrs={'class':'textareaclass'}),
        }