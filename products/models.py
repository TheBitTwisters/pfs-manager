from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import Truncator


class Product(models.Model):
    category = models.CharField(max_length=15, blank=False)
    code = models.CharField(max_length=15, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    design = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(null=True, blank=True)
    datetime_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '[' + self.code + '] ' + self.name

    def form(self, form):
        self.code = form.get('code', '')
        self.name = form.get('name', '')
        self.description = form.get('description', '')
        self.design = form.get('design', '')
        self.price = form.get('price', 0.00)

    def is_valid(self):
        if not self.name:
            return False
        return True

    def short_description(self, word_count=15):
        return Truncator(self.description).words(word_count)

    def print_price(self):
        return "{0:,.2f}".format(self.price)
