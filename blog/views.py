from django.shortcuts import render
from django.views.generic import ListView
from .models import HumanitasPost

# Create your views here.


class HumanitasPostView(ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    context_object_name = 'humanitas_post'
    template_name = 'blog/humanitas-blog.html'
    paginate_by = 8
