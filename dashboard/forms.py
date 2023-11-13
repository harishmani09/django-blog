from django import forms
from blogs.models import Category,Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('title','category','blog_body','featured_image','short_description','status','is_featured',)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','is_staff','is_active','is_superuser', 'groups','user_permissions')
        
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','is_staff','is_active','is_superuser', 'groups','user_permissions')