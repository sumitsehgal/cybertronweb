from django.db import models
from django.utils import timezone
import os
from django.utils.safestring import mark_safe
from django import forms


class Skill(models.Model):
    # title = models.CharField(max_length=200, help_text="Change")
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='upload', null=True)

    def __str__(self):
        return self.title

    def preview(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/upload', os.path.basename(str(self.thumbnail)))))

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='upload', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def preview(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/upload', os.path.basename(str(self.thumbnail)))))


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='upload')
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    categories = models.ManyToManyField(Category)
    # images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

    def preview(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/upload', os.path.basename(str(self.thumbnail)))))

    # def image_preview(self):
    #     print(self.images.all())

class Image(models.Model):
    file = models.ImageField(upload_to='upload')
    position = models.PositiveSmallIntegerField(default=0)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return str(self.file)
        # print(str(self.file))
        # return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/upload', os.path.basename(str(self.file)))))

class ProjectForm(forms.ModelForm):
    pass
