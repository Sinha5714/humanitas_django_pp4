"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
]
