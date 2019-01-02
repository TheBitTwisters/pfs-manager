from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import Truncator


class Quote(models.Model):
    number = models.CharField(max_length=15, blank=False, unique=True)
    person_name = models.CharField(max_length=128, blank=False)
    person_phone = models.CharField(max_length=30, blank=False)
    person_address = models.TextField(blank=True)
    person_deceased_relationship = models.CharField(max_length=30, blank=False)
    contact_name = models.CharField(max_length=128, blank=False)
    contact_phone = models.CharField(max_length=30, blank=False)
    deceased_name = models.CharField(max_length=128, blank=False)
    deceased_date_birth = models.DateField(default=timezone.localdate)
    deceased_date_death = models.DateField(default=timezone.localdate)
    document_type = models.CharField(max_length=15, blank=False)
    document_file = models.FileField(upload_to='documents', default='', blank=True)
    date = models.DateField(default=timezone.localdate)
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
        return '[' + self.number + '] ' + self.deceased_name

    def form(self, form):
        self.number = form.get('number', '0')
        self.person_name = form.get('person_name', '')
        self.person_phone = form.get('person_phone', '')
        self.person_address = form.get('person_address', '')
        self.person_deceased_relationship = form.get('person_deceased_relationship', '')
        self.contact_name = form.get('contact_name', '')
        self.contact_phone = form.get('contact_phone', '')
        self.deceased_name = form.get('deceased_name', '')
        self.deceased_date_birth = form.get('deceased_date_birth', timezone.localdate)
        self.deceased_date_death = form.get('deceased_date_death', timezone.localdate)
        self.document_type = form.get('document_type', '')
        self.date = form.get('date', timezone.localdate)
        self.delivery_datetime = form.get('delivery_datetime', timezone.now)
        self.delivery_notes = form.get('delivery_notes', '')
        self.pickup_datetime = form.get('pickup_datetime', timezone.now)
        self.pickup_notes = form.get('pickup_notes', '')

    def is_valid(self):
        if not self.number:
            return False
        if not self.person_name:
            return False
        return True
