from django.db import models


class University(models.Model):
    name = models.CharField(max_length=120, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=120)

    def __unicode__(self):
        return f'{self.id}. {self.abbreviation}'

    def __str__(self):
        return f'{self.id}. {self.abbreviation}'

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
