from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """
    Profile model used as an account
    for each registered user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('profile_page', kwargs={'pk': self.pk})


class Contact(models.Model):
    """
    a class for the Contact model
    """
    message_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True
                             )
    name = models.CharField(
        max_length=50,
        null=True
    )
    email = models.EmailField(
        max_length=100,
        default=""
    )
    message = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name
