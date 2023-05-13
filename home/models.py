from django.db import models

# Create your models here.

class Profile(models.Model):
    """
    Class model for profile of the user
    """
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image=models.CloudinaryField('image', default='profile_pic')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)