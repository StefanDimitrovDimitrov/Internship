# Generated by Django 3.2.6 on 2021-08-18 08:40

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('internship_app', '0005_alter_internship_ad_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedtracking',
            name='applied_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='internship_ad',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 8, 40, 38, 508182, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='internship_ad',
            name='modified_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]