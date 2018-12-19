from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Log(models.Model):
    object = models.CharField(max_length=50, blank=False)
    object_id = models.IntegerField(default=0)
    action = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
