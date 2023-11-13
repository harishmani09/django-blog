from django.shortcuts import get_object_or_404, render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,PostForm
from django.template.defaultfilters import slugify


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'cat_count':category_count,
        'blog_count': blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html') 

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash-category')
    form = CategoryForm()
    context= {
        'form':form
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('dash-category')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('dash-category')

@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'dashboard/posts.html', context)

# @login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) 
            post.save()
            return redirect('posts')
        else:
            print('form is not valid')
            print(form.errors)
            
    form = PostForm()
    # print(form)
    context = {
        'form':form,
        
    }
    return render(request, 'dashboard/add_post.html', context)

@login_required(login_url='login')
def edit_posts(request,pk):
    form = PostForm()
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        
    form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'dashboard/edit_posts.html', context)


@login_required(login_url='login')
def delete_posts(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    # posts = Blog.objects.all()
    post.delete()
    return redirect('posts')