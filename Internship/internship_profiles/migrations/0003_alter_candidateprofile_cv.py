# Generated by Django 3.2.6 on 2021-08-19 08:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internship_profiles', '0002_auto_20210819_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='CV',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
