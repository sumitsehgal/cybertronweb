# Generated by Django 2.2.7 on 2019-12-02 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]