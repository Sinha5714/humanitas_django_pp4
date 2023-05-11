from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
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


class HumanitasPostView(ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    context_object_name = 'humanitas_post'
    template_name = 'stories/humanitas-blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HumanitasPostView, self).get_context_data(
            *args, **kwargs)
        context['title'] = 'Our Stories'
        return context


class BlogDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = HumanitasPost
    template_name = 'stories/blog_detail.html'
    context_object_name = 'post'
    form = CommentForm
    success_url = 'blog/<int:pk>'

    def post(self, request, pk):
        post = HumanitasPost.objects.get(id=pk)
        ied = pk
        comments = Comment.objects.filter(humanitas_post=post).order_by("-pk")

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST or None)
            if comment_form.is_valid():
                content = request.POST.get('content')
                comment = Comment.objects.create(
                    humanitas_post=post, author=request.user, content=content)
                comment.save()
                return redirect(post.get_absolute_url())
        else:
            comment_form = CommentForm()

        context = {
            'title': 'Story Details',
            'comments': comments,
            'ied': ied,
            'comment_form': comment_form
        }
        return render(request, 'stories/blog_detail.html', context)


@login_required
def deletecomment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    messages.success(request, f'Comment deleted!')
    return redirect(comment.post.get_absolute_url())


class HumanitasPostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = HumanitasPost
    fields = ['title', 'body', 'cover_image']
    template_name = 'stories/add_blog.html'
    success_url = '/blog'
    success_message = 'Your story is added successfully!'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class HumanitasPostUpdate(LoginRequiredMixin, SuccessMessageMixin,  UserPassesTestMixin, UpdateView):
    model = HumanitasPost
    fields = ['title', 'body', 'cover_image']
    success_url = '/blog'
    success_message = 'Your story has been updated successfully!'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


class HumanitasPostDelete(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = HumanitasPost
    success_url = '/blog'
    success_message = 'Your story has been deleted successfully!'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False
