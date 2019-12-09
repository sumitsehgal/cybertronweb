# Generated by Django 2.2.7 on 2019-12-09 12:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(null=True, upload_to='upload')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(null=True, upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('thumbnail', models.ImageField(upload_to='upload')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('categories', models.ManyToManyField(to='portfolio.Category')),
                ('skills', models.ManyToManyField(to='portfolio.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='upload')),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.Project')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
