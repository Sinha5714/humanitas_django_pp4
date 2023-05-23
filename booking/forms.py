from django import forms
from django.contrib.auth.models import User
from .models import Booking
import datetime
from django.utils import timezone


class BookingForm(forms.ModelForm):
    date = forms.DateField(disabled=True)
    timeblock = forms.CharField(disabled=True)
    helptype = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Human Rights"}),
        required=False
    )

    class Meta:
        model = Booking
        fields = ["date", "timeblock", "helptype"]

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
    
