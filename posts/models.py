from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()