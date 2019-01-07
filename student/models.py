from django.db import models
from django.urls import reverse

# Create your models here.


class Student(models.Model):
    STATE_OF_STUDDING = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    index = models.CharField(max_length=6)
    profile = models.CharField(max_length=120)
    status = models.TextField(max_length=10, choices=STATE_OF_STUDDING)
    deficit = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse("student:student-details", kwargs={"id": self.id})
