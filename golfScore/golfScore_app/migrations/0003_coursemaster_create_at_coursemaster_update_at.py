# Generated by Django 5.1.1 on 2024-10-23 11:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfScore_app', '0002_coursemaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemaster',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='coursemaster',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
