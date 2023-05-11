"""
Module for blog urls 
"""
from django.urls import path
from .views import HumanitasPostView, HumanitasPostCreate
from . import views

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('blog/<int:pk>/', views.blog_detail,
         name='blog_details'),
    path('blog/new',
         HumanitasPostCreate.as_view(), name='add_blog'),
]
