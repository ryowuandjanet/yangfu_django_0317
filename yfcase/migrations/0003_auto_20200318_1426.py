# Generated by Django 3.0.4 on 2020-03-18 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yfcase', '0002_auto_20200318_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='foreclosure_announcement',
        ),
        migrations.RemoveField(
            model_name='case',
            name='object_photos',
        ),
    ]
