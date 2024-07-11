from django.shortcuts import render
from .models import Post
from .forms import SignupForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def user_signup(request):
    if request.method == 'POST':        
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Validation failed!!")
    else:
        form = SignupForm()

    return render(request,'signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,("Invalid username or passoword"))
            return redirect('login')

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request,'profile.html')
