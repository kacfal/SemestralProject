from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(blank=True, max_length=120)
    last_name = models.CharField(blank=True, max_length=120)
    index = models.CharField(blank=True, max_length=6)
    profile = models.CharField(blank=True, max_length=120)
    status = models.BooleanField(default=True)

