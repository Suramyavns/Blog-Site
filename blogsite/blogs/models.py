from django.db import models
import django.utils.timezone as timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class topic(models.Model):
    topicname = models.CharField(max_length=20)
    def __str__(self):
        return self.topicname

class blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to="thumbnails",blank=True)
    topicname = models.ForeignKey(topic,on_delete=models.SET_NULL,null=True)
    def bodypart(self):
        return self.body[:50]


    