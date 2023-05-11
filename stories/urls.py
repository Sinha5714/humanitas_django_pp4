"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView, BlogDetailView, HumanitasPostCreate
from . import views

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('stories/<int:pk>/', BlogDetailView.as_view(),
         name='blog_details'),
    path('stories/new',
         HumanitasPostCreate.as_view(), name='add_blog'),
]
