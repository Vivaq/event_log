from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class LogAttempts(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(default='unknown', max_length=255)
    event_date = models.DateField(default='1980-01-01')
    succeeded = models.BooleanField(default=False)


class Errors(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(default='unknown', max_length=255)
    event_date = models.DateField(default='1980-01-01')
    why = models.CharField(default='unknown', max_length=255)
    danger = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])


class ConfigurationChanged(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(default='unknown', max_length=255)
    event_date = models.DateField(default='1980-01-01')
    description = models.CharField(default='None', max_length=255)
