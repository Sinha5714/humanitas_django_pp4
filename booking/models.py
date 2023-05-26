from django.db import models
from datetime import date
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

TIMEBLOCK_CHOICES = (
    ("10:00", "10:00-10:20"),
    ("10:30", "10:30-10:50"),
    ("11:00", "11:00-11:20"),
    ("11:30", "11:30-11:50"),
    ("12:00", "12:00-12:20"),
    ("15:00", "15:00-15:20"),
    ("15:30", "15:30-15:50"),
)


class Booking(models.Model):
    """
    Class model for booking a call
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    timeblock = models.CharField(
        max_length=10, choices=TIMEBLOCK_CHOICES, default="10:00")
    helptype = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user.username}: {self.date} ({self.timeblock})"

    def clean(self):
        if Booking.objects.filter(date=self.date,
                                  timeblock=self.timeblock).exists():
            raise ValidationError("That date & time is already booked!")
