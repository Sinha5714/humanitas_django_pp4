from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import HumanitasPost
from .forms import CommentForm, BlogForm

# Create your views here.


class HumanitasPostView(generic.ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    context_object_name = 'humanitas_post'
    template_name = 'blog/humanitas-blog.html'


class BlogDetailView(View):
    """
    Detail view for each blogpost
    and added comments
    """
    model = HumanitasPost
    context_object_name = 'posts'
    template_name = 'blog/blog_detail.html'
    slug_field = 'slug'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        """
        overriding the post method and
        saving the user comment
        """
        form = CommentForm(request.POST)
        if form.is_valid():
            humanitas_post = self.get_object()
            form.instance.author = request.user
            form.instance.humanitas_post = humanitas_post
            form.save()
            messages.success(request, 'YOU ADDED A NEW COMMENT')
            return HttpResponseRedirect(
                reverse('blog_details', kwargs={'pk': humanitas_post.pk}))
        else:
            form = CommentForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddBlog(generic.CreateView):

    model = HumanitasPost
    form_class = BlogForm
    template_name = 'blog/add_blog.html'
    success_message = 'Your story added succesfully'
