from django.db import models

# Create your models here.


class Student(models.Model):
    STATE_OF_STUDDING = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(blank=True, max_length=120)
    last_name = models.CharField(blank=True, max_length=120)
    index = models.CharField(blank=True, max_length=6)
    profile = models.CharField(blank=True, max_length=120)
    status = models.CharField(max_length=10, choices=STATE_OF_STUDDING)

