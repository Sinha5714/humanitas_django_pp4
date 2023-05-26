"""
Module for stories urls
"""
from django.urls import path
from .views import (HumanitasPostView,
                    HumanitasUserPostView,
                    HumanitasPostCreate,
                    HumanitasPostUpdate,
                    HumanitasPostDelete)
from . import views

urlpatterns = [
    path('', HumanitasPostView.as_view(), name='humanitas_blog_page'),
    path('my_stories', HumanitasUserPostView.as_view(),
         name='my_stories'),
    path('<int:pk>/', views.post_detail,
         name='blog_details'),
    path('comment/<int:id>', views.deletecomment, name='blog_comment'),
    path('stories/new',
         HumanitasPostCreate.as_view(), name='add_blog'),
    path('<int:pk>/update/',
         HumanitasPostUpdate.as_view(), name='update_blog'),
    path('<int:pk>/delete/',
         HumanitasPostDelete.as_view(), name='delete_blog'),
]
