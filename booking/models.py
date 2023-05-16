from django.db import models
from datetime import date
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):

    TIMEBLOCK_CHOICES = (
        ("A", "10:00-10:20"),
        ("B", "10:30-10:50"),
        ("C", "11:00-11:20"),
        ("D", "11:30-11:50"),
        ("E", "12:00-12:20"),
        ("F", "15:00-15:20"),
        ("G", "15:30-15:50"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    timeblock = models.CharField(
        max_length=10, choices=TIMEBLOCK_CHOICES, default="A")
    helptype = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user.username}: {self.date} ({self.timeblock})"

    
