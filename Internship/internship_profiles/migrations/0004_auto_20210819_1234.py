# Generated by Django 3.2.6 on 2021-08-19 09:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_profiles', '0003_alter_candidateprofile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='CV',
            field=models.FileField(blank=True, upload_to='intern_cv'),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='company_logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
