"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView, BlogDetailView, PostLike

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('<slug:slug>/', BlogDetailView.as_view(),
         name='blog_details'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
]
