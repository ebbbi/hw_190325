from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(default=timezone.now)
    eyes=models.TextField(default='')
    lip=models.TextField(default='')
    face=models.TextField(default='')
    writer=models.TextField(default='')
    category=models.CharField(max_length=255, default='')
    image=models.ImageField(upload_to='images/', blank=True)
