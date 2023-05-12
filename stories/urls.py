"""
Module for blog urls 
"""
from django.urls import path
from .views import (HumanitasPostView, BlogDetailView,
                    HumanitasPostCreate, HumanitasPostUpdate,
                    HumanitasPostDelete)
from . import views

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('stories/<int:pk>', BlogDetailView.as_view(),
         name='blog_details'),
    path('stories/new',
         HumanitasPostCreate.as_view(), name='add_blog'),
    path('stories/<int:pk>/update/',
         HumanitasPostUpdate.as_view(), name='update_blog'),
    path('stories/<int:pk>/delete/',
         HumanitasPostDelete.as_view(), name='delete_blog'),
]
