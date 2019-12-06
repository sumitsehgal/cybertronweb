from django.db import models
from django.utils import timezone


class Skill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='upload', null=True)

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='upload', null=True)

class Image(models.Model):
    file = models.ImageField(upload_to='upload')
    position = models.PositiveSmallIntegerField(default=0)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='upload')
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)
