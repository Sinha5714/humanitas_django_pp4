from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label="Primary email")

    class Meta:
        model = Profile
        fields = ['profile_image', 'email']
