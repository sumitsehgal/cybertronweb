from django.db import models
from django.utils import timezone


class Skill(models.Model):
    title = models.CharField(max_length=200, help_text="Change")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='upload', null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='upload', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Image(models.Model):
    file = models.ImageField(upload_to='upload')
    position = models.PositiveSmallIntegerField(default=0)
    
    # def __str__(self):
    #     return self.title

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

    def __str__(self):
        return self.title