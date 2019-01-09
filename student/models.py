from django.db import models
from django.urls import reverse


class Profile(models.Model):
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return f'{self.id}. {self.name}'

    def __str__(self):
        return f'{self.id}. {self.name}'


class Department(models.Model):
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=10)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __unicode__(self):
        return f'{self.id}. {self.abbreviation}'

    def __str__(self):
        return f'{self.id}. {self.abbreviation}'


class University(models.Model):
    name_of_university = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=10)
    city = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __unicode__(self):
        return f'{self.id}. {self.abbreviation}'

    def __str__(self):
        return f'{self.id}. {self.abbreviation}'

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Student(models.Model):
    STATE_OF_STUDDING = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    university = models.ManyToManyField(University)
    index = models.CharField(max_length=6)
    status = models.TextField(choices=STATE_OF_STUDDING)
    deficit = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse("student:student-details", kwargs={"id": self.id})

    def __unicode__(self):
        return f'{self.id}. {self.name}'

    def __str__(self):
        return f'{self.id}. {self.name}'
