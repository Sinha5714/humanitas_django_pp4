from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


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

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title + ' | ' + str(self.creator)

    def get_absolute_url(self):
        return reverse("humanitas_blog_page")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Model fo comments from users
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    humanitas_post = models.ForeignKey(
        HumanitasPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk': self.humanitas_post.pk})

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.author + '|commented: ' + self.content
