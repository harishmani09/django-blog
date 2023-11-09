from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog, Category
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