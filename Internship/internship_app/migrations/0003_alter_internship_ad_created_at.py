# Generated by Django 3.2.6 on 2021-08-17 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship_ad',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 20, 21, 45, 178584), editable=False),
        ),
    ]