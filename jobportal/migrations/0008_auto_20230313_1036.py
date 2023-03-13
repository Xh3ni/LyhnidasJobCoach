# Generated by Django 3.2.18 on 2023-03-13 10:36

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_auto_20230313_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True),
        ),
    ]