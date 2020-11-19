from django.db import models
import datetime


class Project(models.Model):
    name = models.CharField(max_length=255)
    descr = models.TextField(null=True)
    added_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default=(datetime.date.today() + datetime.timedelta(weeks=2)))
    done = models.BooleanField(default=False)


class Task(models.Model):
    name = models.CharField(max_length=255)
    descr = models.TextField(null=True)
    added_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default=(datetime.date.today() + datetime.timedelta(weeks=2)))
    done = models.BooleanField(default=False)
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
