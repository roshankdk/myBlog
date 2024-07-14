from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import SignupForm, LoginForm, PostForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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


# creating the new post using class based view {new-story}
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'index.html'
    form_class = PostForm
    model = Post
    template_name = 'newstory.html'
    success_url = reverse_lazy('index')

@login_required
def newstory(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            author, created = Author.objects.get_or_create(user = request.user)
            print(author)
            post.author = author
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request,'newstory.html', {'form':form})
