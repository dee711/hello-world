from __future__ import unicode_literals

from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Create your models here.
