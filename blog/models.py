from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class HumanitasPost(models.Model):
    """
    HumanitasPost model used for each blog posted by users
    """

    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="humanitas_posts")
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    cover_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.creator)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model fo comments from users
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    humanitas_post = models.ForeignKey(
        HumanitasPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=60)
    content = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name + '|commented: ' + self.content
