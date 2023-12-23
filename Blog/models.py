from django.db import models
from django.urls import reverse

# Create your models here.


class BlogPost(models.Model):

    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    content = models.TextField()
    isPublished= models.BooleanField(default=False)

