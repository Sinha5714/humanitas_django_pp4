from django import forms
from django.contrib.auth.models import User
from .models import Booking
import datetime


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

    def clean(self):
        if Booking.objects.filter(date=self.date,
                                  timeblock=self.timeblock).exists():
            raise forms.ValidationError("That date & time is already booked!")
