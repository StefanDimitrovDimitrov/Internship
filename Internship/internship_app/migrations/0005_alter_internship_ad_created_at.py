# Generated by Django 3.2.6 on 2021-08-18 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_app', '0004_alter_internship_ad_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship_ad',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 10, 40, 14, 235125), editable=False),
        ),
    ]
