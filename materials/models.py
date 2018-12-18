from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Material(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    date_purchased = models.DateField(default=timezone.localdate)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_deleted = models.DateTimeField(null=True, blank=True)

    def form(self, form):
        self.name = form.get('name', '')
        self.description = form.get('description', '')
        self.quantity = form.get('quantity', 0)
        self.date_purchased = form.get('date_purchased', datetime.date.today)

    def is_valid(self):
        if not self.name:
            return False
        return True
