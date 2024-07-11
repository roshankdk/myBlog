from django.shortcuts import render
from .models import Post
from .forms import SignupForm
from django.shortcuts import redirect

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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Validation failed!!")
    else:
        form = SignupForm()

    return render(request,'signup.html',{'form':form})


def profile(request):
    return render(request,'profile.html')

def login(request):
    return render(request,'login.html')