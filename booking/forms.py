from django import forms
from django.contrib.auth.models import User
from .models import Booking


class BookingForm(forms.ModelForm):
    date = forms.DateField(disabled=True)
    helptype = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Human Rights"}), required=False
    )

    class Meta:
        model = Booking
        fields = ["date", "timeblock", "helptype"]
