# Generated by Django 3.1.3 on 2020-11-18 11:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descr', models.TextField()),
                ('added_date', models.DateField(default=datetime.date(2020, 11, 18))),
                ('end_date', models.DateField(default=datetime.date(2020, 12, 2))),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descr', models.TextField()),
                ('added_date', models.DateField(default=datetime.date(2020, 11, 18))),
                ('end_date', models.DateField(default=datetime.date(2020, 12, 2))),
                ('done', models.BooleanField(default=False)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.project')),
            ],
        ),
    ]