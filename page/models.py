from django.db import models
from django.utils.text import slugify
from djrichtextfield.models import RichTextField

# Create your models here.

from Services.models import Services
from slider.models import Slider
    
class Page(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Service = models.ManyToManyField(Services)
    Slider = models.ManyToManyField(Slider)
    Content = RichTextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title