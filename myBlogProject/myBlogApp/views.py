from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import SignupForm, LoginForm, PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Author

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'index.html',context)

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.all()
    context = {
        'post':post,
        'comments':comments,
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

@login_required
def newstory(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            user = request.user
            if not Author.objects.filter(user=user).exists():
                author = Author.objects.create(user=user)
            else:
                author = Author.objects.get(user=user)
            post.author = author
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request,'newstory.html', {'form':form})


def comment(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('post',pk=post.pk)
    else:
        form = CommentForm(request.POST)

    return render(request,'comment.html',{'form':form})