"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView
from . import views

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('blog/<int:pk>', views.post_detail,
         name='blog_details'),
]
