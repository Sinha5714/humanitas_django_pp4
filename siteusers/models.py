from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.


class Profile(models.Model):
    """
    Profile model used as an account
    for each registered user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    profile_image = CloudinaryField('image', default='placeholder')
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
