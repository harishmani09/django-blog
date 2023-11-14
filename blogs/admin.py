from django.contrib import admin
from .models import Category, Blog, Comment 
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','is_featured','featured_image','status','updated_at')
    search_fields = ('id','title','author__username','status','category__category_name')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)

# admin.site.register(About)
# admin.site.register(Social)