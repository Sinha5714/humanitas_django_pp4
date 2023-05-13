from django.db import models
from datetime import date
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):

    TIMEBLOCK_CHOICES = (
        ("A", "10:00-11:00"),
        ("B", "11:00-12:00"),
        ("C", "12:00-13:00"),
        ("D", "13:00-14:00"),
        ("E", "14:00-15:00"),
        ("F", "15:00-16:00"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    timeblock = models.CharField(
        max_length=10, choices=TIMEBLOCK_CHOICES, default="A")
    helptype = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user.username}: {self.date} ({self.timeblock})"
