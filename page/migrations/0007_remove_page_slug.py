# Generated by Django 2.2.7 on 2019-11-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20191129_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
