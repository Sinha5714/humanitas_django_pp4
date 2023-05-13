from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=60, required=True)
    subject = forms.CharField(max_length=60, required=False)
    message = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 5}
    ), required=True)
