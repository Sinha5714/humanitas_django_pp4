from django.shortcuts import (render, get_object_or_404,
                              reverse, redirect)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
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
    A class view to view a list of all stories
    """
    model = HumanitasPost
    queryset = HumanitasPost.objects.filter(status=1).order_by("-updated_on")
    context_object_name = 'humanitas_post'
    template_name = 'stories/humanitas-stories.html'


class HumanitasUserPostView(ListView):
    """
    A class view to view a list of all stories 
    created by logged in User
    """
    model = HumanitasPost
    queryset = HumanitasPost.objects.filter(status=1).order_by("-updated_on")
    context_object_name = 'humanitas_post'
    template_name = 'stories/my_stories.html'


@login_required
def post_detail(request, pk):
    post = HumanitasPost.objects.get(id=pk)
    comments = Comment.objects.filter(humanitas_post=post).order_by("-pk")

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                humanitas_post=post, author=request.user, content=content)
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm

    context = {
        'title': 'Story Details',
        'comments': comments,
        'object': post,
        'comment_form': comment_form
    }
    return render(request, 'stories/stories_detail.html', context)


@ login_required
def deletecomment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return redirect(comment.humanitas_post.get_absolute_url())


class HumanitasPostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A class view to create a new story by user
    """
    model = HumanitasPost
    fields = ['title', 'body', 'cover_image']
    template_name = 'stories/add_story.html'
    success_url = '/stories'
    success_message = 'Your story is added successfully!'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class HumanitasPostUpdate(LoginRequiredMixin,
                          SuccessMessageMixin,
                          UserPassesTestMixin,
                          UpdateView):
    """
    A class view to update the existing story by user
    """
    model = HumanitasPost
    fields = ['title', 'body', 'cover_image']
    success_url = '/stories'
    template_name = 'stories/add_story.html'
    success_message = 'Your story has been updated successfully!'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


class HumanitasPostDelete(LoginRequiredMixin,
                          SuccessMessageMixin,
                          UserPassesTestMixin,
                          DeleteView):
    """
    A class view to delete the story by user
    """
    model = HumanitasPost
    success_url = '/stories'
    template_name = 'stories/story_delete_confirm.html'
    success_message = 'Your story has been deleted successfully!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(HumanitasPostDelete, self).delete(request,
                                                       *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False
