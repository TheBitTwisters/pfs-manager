from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def form(self, form):
        self.name = form.get('name', '')

    def is_valid(self):
        if not self.name:
            return False
        return True


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def form(self, form):
        self.name = form.get('name', '')

    def is_valid(self):
        if not self.name:
            return False
        return True
