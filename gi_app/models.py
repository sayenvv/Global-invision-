from django.db import models

# Create your models here.
class Contact_book(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    