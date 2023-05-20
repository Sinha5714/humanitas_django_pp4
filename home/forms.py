from .models import Profile, Contact
from django import forms



class ProfileForm(forms.ModelForm):
    """
    A class for the profile creation form
    """

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']
