# Generated by Django 2.2.7 on 2019-11-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_src',
            name='src',
            field=models.ImageField(upload_to=''),
        ),
    ]
