# Generated by Django 5.1.1 on 2024-10-25 15:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfScore_app', '0002_alter_golfhousemaster_house_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_address',
            field=models.CharField(max_length=255, verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_city',
            field=models.CharField(max_length=100, verbose_name='市町村区'),
        ),
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ゴルフ場ID'),
        ),
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_name',
            field=models.CharField(max_length=255, verbose_name='ゴルフ場名'),
        ),
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_phone_number',
            field=models.CharField(max_length=11, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_prefecture',
            field=models.CharField(max_length=40, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='golfhousemaster',
            name='house_zipcode',
            field=models.CharField(max_length=8, verbose_name='郵便番号'),
        ),
    ]
