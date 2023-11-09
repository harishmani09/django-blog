from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name ='index'),
    path('<int:category_id>', views.posts_by_category, name="posts_by_category"),
]
