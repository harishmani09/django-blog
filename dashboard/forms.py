from django import forms
from blogs.models import Category,Blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('title','category','blog_body','featured_image','short_description','status','is_featured',)