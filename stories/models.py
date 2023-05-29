# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class HumanitasPost(models.Model):
    """
    HumanitasPost model used for each blog posted by users
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True, blank=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="humanitas_posts")
    body = models.TextField()
    cover_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title + ' | ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Model for comments from users
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    humanitas_post = models.ForeignKey(
        HumanitasPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment on {} by {}'.format(self.humanitas_post.title,
                                            self.author.username)
