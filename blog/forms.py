from .models import Comment, HumanitasPost
from django import forms


class CommentForm(forms.ModelForm):
    """
    Class for comment creation
    """

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'md-textarea form-control comment-text',
                'placeholder': 'your comment....',
                'rows': '4',
                'id': 'comment',
            }
        ),
        label='comment:'
    )

    class Meta:
        model: Comment
        fields = ['content',]


class BlogForm(forms.ModelForm):
    """
    A class for the blog creation form
    """
    class Meta:
        model = HumanitasPost
        fields = ('title', 'cover_image', 'body',)
