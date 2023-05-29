# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# Internal:
from .models import Comment, HumanitasPost


class CommentForm(forms.ModelForm):
    """
    Class for comment creation
    """
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here!',
            'rows': 4,
            'cols': 50
        }))

    class Meta:
        model = Comment
        fields = ['content']


class BlogForm(forms.ModelForm):
    """
    A class for the blog creation form
    """

    class Meta:
        model = HumanitasPost
        fields = ('title', 'cover_image', 'body',)

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Story Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
