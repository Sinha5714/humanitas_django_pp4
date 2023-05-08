from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
    paginate_by = 8


class BlogDetailView(View):
    """
    Detail view for each blogpost
    and added comments
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = HumanitasPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "humanitas-blog-details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
