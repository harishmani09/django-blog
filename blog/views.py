from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, Blog
from assignments.models import About

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

