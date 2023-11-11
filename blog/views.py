from django.shortcuts import redirect, render
from django.http import HttpResponse
from blogs.models import Category, Blog
from assignments.models import About
from .forms import RegistrationForm, AuthenticationForm
from django.contrib import auth

def home(request):
    # categories = Category.objects.all()
    featured_blog = Blog.objects.filter(is_featured=True,status='published')
    posts = Blog.objects.filter(is_featured=False, status='published')
    
    # fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured':featured_blog, 
        'posts':posts,
        'about':about,
    }
    
    
    return render(request,'blog/index.html',context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request,'blog/register.html',context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
                        
    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'blog/login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('home')