from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comnt = models.CharField(max_length=128, null=True)
