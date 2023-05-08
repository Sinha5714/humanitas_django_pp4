from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import HumanitasPost
from .forms import CommentForm

# Create your views here.


class HumanitasPostView(ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    context_object_name = 'humanitas_post'
    template_name = 'blog/humanitas-blog.html'
    paginate_by = 8


class BlogDetailView(DetailView):
    """
    Detail view for each blogpost
    and added comments
    """
    model = HumanitasPost
    context_object_name = 'post'
    template_name = 'flow_blog/humanitas-blog-details.html'
    slug_field = 'slug'
    form = CommentForm
