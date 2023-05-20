from .models import Profile, Contact
from django import forms


class ContactUsForm(forms.ModelForm):

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
    A class for the profile creation form
    """

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']
