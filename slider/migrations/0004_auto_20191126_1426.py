# Generated by Django 2.2.7 on 2019-11-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0003_auto_20191126_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_src',
            name='Text_1',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_src',
            name='Text_2',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_src',
            name='Text_3',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_src',
            name='label_2',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_src',
            name='label_3',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
    ]