"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView, BlogDetailView, AddBlog

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('blog/blog/<int:pk>', BlogDetailView.as_view(),
         name='blog_details'),
    path('blog/add_blog/', AddBlog.as_view(), name='add_blog'),
]
