from django.db import models
from django.contrib.auth.models import User
import datetime


class Coffin(models.Model):
    code = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    colors = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[' + self.code + '] ' + self.name

    def form(self, form):
        self.code = form.get('code', '')
        self.name = form.get('name', '')
        self.description = form.get('description', '')
        self.colors = form.get('colors', '')
        self.price = form.get('price', 0.00)

    def is_valid(self):
        if not self.name:
            return False
        if not self.colors:
            return False
        return True


class Service(models.Model):
    code = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[' + self.code + '] ' + self.name

    def form(self, form):
        self.code = form.get('code', '')
        self.name = form.get('name', '')
        self.description = form.get('description', '')
        self.price = form.get('price', 0.00)

    def is_valid(self):
        if not self.name:
            return False
        return True
