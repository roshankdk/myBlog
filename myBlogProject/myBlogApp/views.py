from django.shortcuts import render
from .models import Post
from .forms import singUpForm
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'index.html',context)

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post':post
    }
    return render(request,'post_details.html', context)

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)


    return render(request,'signup.html')