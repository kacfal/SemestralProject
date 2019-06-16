from django.db import models
from django.urls import reverse
from university.models import University


class Student(models.Model):
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, related_name='universities')
    department = models.CharField(max_length=120)
    profile = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    index = models.DecimalField(max_digits=999999, decimal_places=0, unique=True)
    deficit = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse("student:student-details", kwargs={"id": self.id})

    def __unicode__(self):
        return f'{self.id}. {self.name}'

    def __str__(self):
        return f'{self.id}. {self.name}'
