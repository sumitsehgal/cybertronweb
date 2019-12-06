from django.db import models
import os
from django.utils.safestring import mark_safe

# Create your models here.

class Services(models.Model):
    Icon = models.ImageField(upload_to='Images/Services')
    Title = models.CharField(max_length=100)
    Heading = models.CharField(max_length=100)
    Sub_Heading = models.CharField(max_length=100)
    Main_Text = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.Title

    def Icon_Preview(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/Images/Services', os.path.basename(str(self.Icon)))))
