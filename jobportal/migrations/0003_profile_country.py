# Generated by Django 3.2.18 on 2023-03-12 01:21

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0002_appliedjobs_profile_savedjobs_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]