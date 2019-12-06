# Generated by Django 2.2.7 on 2019-11-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='portfolio.Category'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='portfolio.Skill'),
        ),
    ]