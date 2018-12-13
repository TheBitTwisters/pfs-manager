from django.db import models
from django.contrib.auth.models import User
import datetime


class Material(models.Model):
    code = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    date_purchased = models.DateField(default=datetime.date.today)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[' + self.code + '] ' + self.name

    def form(self, form):
        self.code = form.get('code', '')
        self.name = form.get('name', '')
        self.description = form.get('description', '')
        self.quantity = form.get('quantity', 0)
        self.date_purchased = form.get('date_purchased', datetime.date.today)

    def is_valid(self):
        if not self.code:
            return False
        if not self.name:
            return False
        return True
