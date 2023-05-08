from .models import Comment, HumanitasPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment
        fields = ('content',)


class BlogForm(forms.ModelForm):
    """
    A class for the blog creation form
    """
    class Meta:
        model = HumanitasPost
        fields = ('title', 'cover_image', 'body',)
