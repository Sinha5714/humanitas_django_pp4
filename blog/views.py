from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import HumanitasPost
from .forms import CommentForm

# Create your views here.


class HumanitasPostView(generic.ListView):
    """
    A class view to view a list of all posts
    """
    model = HumanitasPost
    queryset = HumanitasPost.objects.filter(status=1).order_by("-created_on")
    context_object_name = 'humanitas_post'
    template_name = 'blog/humanitas-blog.html'
    paginate_by = 6


class BlogDetailView(View):
    """
    Detail view for each blogpost
    and added comments
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = HumanitasPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment_form = CommentForm()
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "commented": False,
                "comment_form": comment_form
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = HumanitasPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm

        return render(
            request,
            "blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )
