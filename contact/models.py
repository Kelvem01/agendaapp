from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length= 50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150, blank = True)
    created_date = models.DateTimeField(default= timezone.now)
    description = models.TextField(blank=True)