# Generated by Django 3.2.5 on 2021-07-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_profiles', '0007_auto_20210722_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
