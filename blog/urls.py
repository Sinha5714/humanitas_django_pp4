"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView, BlogDetailView

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('<slug:slug>/', BlogDetailView.as_view(),
         name='blog_details'),
]
