# Generated by Django 2.2.7 on 2019-11-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]