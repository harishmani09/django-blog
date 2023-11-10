from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models import Q
# Create your views here.

def index(request):
    return HttpResponse('blogs main site being hit')


def posts_by_category(request,category_id):
    cat_posts = Blog.objects.filter(status='published',category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # category = get_object_or_404(Category,pk=category_id)
    context = {
            'category': category,
            'cat_posts' : cat_posts
        }
    return render(request,'blog/posts_by_category.html',context)

def blog_view(request,slug):
    # single_blog = Blog.objects.get(slug=slug, status='published')
    single_blog = get_object_or_404(Blog, slug=slug, status='published')
    context = {
        'single_blog':single_blog
    }
    return render(request, 'blog/blog_view.html',context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword)| Q(short_description__icontains=keyword)| Q(blog_body__icontains=keyword),status='published')
    print(blogs)
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'blog/search.html',context)