from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import Truncator
from products.models import Product


class Quote(models.Model):
    number = models.CharField(max_length=15, blank=False, unique=True)
    date = models.DateField(default=timezone.localdate)
    payment_mode = models.CharField(max_length=30, default='')
    payment_terms = models.CharField(max_length=30, default='')
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    gst = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(null=True, blank=True)
    datetime_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Quote # %s' % self.number


class QuoteProducts(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Client(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=128, blank=False)
    person_phone = models.CharField(max_length=30, blank=False)
    person_address = models.TextField(blank=True)
    person_deceased_relationship = models.CharField(max_length=30, blank=False)
    contact_name = models.CharField(max_length=128, blank=False)
    contact_phone = models.CharField(max_length=30, blank=False)
    deceased_name = models.CharField(max_length=128, blank=False)
    deceased_date_birth = models.DateField(default=timezone.localdate)
    deceased_date_death = models.DateField(default=timezone.localdate)
    delivery_datetime = models.DateTimeField(default=timezone.now)
    delivery_notes = models.TextField(blank=True)
    pickup_datetime = models.DateTimeField(default=timezone.now)
    pickup_notes = models.TextField(blank=True)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(null=True, blank=True)
    datetime_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.quote, self.person_name)

    def form(self, form):
        self.person_name = form.get('person_name', '')
        self.person_phone = form.get('person_phone', '')
        self.person_address = form.get('person_address', '')
        self.person_deceased_relationship = form.get('person_deceased_relationship', '')
        self.contact_name = form.get('contact_name', '')
        self.contact_phone = form.get('contact_phone', '')
        self.deceased_name = form.get('deceased_name', '')
        self.deceased_date_birth = form.get('deceased_date_birth', timezone.localdate)
        self.deceased_date_death = form.get('deceased_date_death', timezone.localdate)
        self.delivery_datetime = form.get('delivery_datetime', timezone.now)
        self.delivery_notes = form.get('delivery_notes', '')
        self.pickup_datetime = form.get('pickup_datetime', timezone.now)
        self.pickup_notes = form.get('pickup_notes', '')

    def is_valid(self):
        if not self.person_name:
            return False
        if not self.contact_name:
            return False
        if not self.deceased_name:
            return False
        return True


class ClientFile(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, blank=False)
    file = models.FileField(upload_to='documents', default='', blank=True)
