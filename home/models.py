from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    """
    Class model for profile of the user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='profile_pic')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
