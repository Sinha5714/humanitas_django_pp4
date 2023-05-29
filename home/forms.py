# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# Internal:
from .models import Profile, Contact


class ContactUsForm(forms.ModelForm):
    """
    A class for the contact form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message')


class ProfileForm(forms.ModelForm):
    """
    A class for the profile update form
    """

    class Meta:
        model = Profile
        fields = ['profile_image', 'first_name', 'last_name', 'email']
