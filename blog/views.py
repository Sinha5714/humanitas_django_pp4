from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import HumanitasPost, Comment
from .forms import CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.


class HumanitasPostView(LoginRequiredMixin, ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    context_object_name = 'humanitas_post'
    template_name = 'blog/humanitas-blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HumanitasPostView, self).get_context_data(
            *args, **kwargs)
        context['title'] = 'My Story'
        return context


@login_required
def post_detail(request, pk):
    post = HumanitasPost.objects.get(id=pk)
    ied = pk
    comments = Comment.objects.filter(post=post).order_by('-pk')

    if request.method == 'POST':
        comment_form = (request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                post=post, user=request.user, content=content)
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            comment_form = CommentForm()
        context = {
            'title': 'Story Details',
            'comments': comments,
            'ied': ied,
            'object': post,
            'comment_form': comment_form
        }
        return render(request, 'blog/blog_detail.html', context)
