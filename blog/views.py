from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Category, Blog

def home(request):
    # categories = Category.objects.all()
    featured_blog = Blog.objects.filter(is_featured=True,status='published')
    posts = Blog.objects.filter(is_featured=False, status='published')
    context = {
        'featured':featured_blog, 'posts':posts
    }
    
    
    return render(request,'blog/index.html',context)

