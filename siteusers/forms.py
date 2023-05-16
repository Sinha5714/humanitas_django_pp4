from django.contrib.auth import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.UserCreationForm):
    email = forms.EmailField(label="Primary email")

    class Meta(forms.UserCreationForm.Meta):
        model = Profile
        fields = ['profile_image', 'email']
