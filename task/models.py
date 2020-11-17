from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=255)
    added_date = models.DateTimeField(default=timezone.now())
    done = models.BooleanField(default=False)
