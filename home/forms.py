from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=60, required=True)
    subject = forms.CharField(max_length=60, required=False)
    message = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 5}
    ), required=True)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
