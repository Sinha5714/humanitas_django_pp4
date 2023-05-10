from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import HumanitasPost, Comment
from .forms import CommentForm

# Create your views here.


class HumanitasPostView(generic.ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    context_object_name = 'humanitas_post'
    template_name = 'blog/humanitas-blog.html'


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
            'title': 'Post Details',
            'comments': comments,
            'ied': ied,
            'object': post,
            'comment_form': comment_form
        }
        return render(request, 'blog/blog_detail.html', context)
