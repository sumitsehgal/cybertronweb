# Generated by Django 2.2.7 on 2019-11-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='Service',
        ),
        migrations.AddField(
            model_name='page',
            name='Service',
            field=models.ManyToManyField(to='Services.Services'),
        ),
    ]
