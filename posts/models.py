from django.db import models

# Create your models here.
class Post(models.Model):
    tltle = models.CharField(max_length=100)
    content = models.TextField()
