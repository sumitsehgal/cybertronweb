from django.db import models
from django.utils.safestring import mark_safe
import os

class Clients(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='Images/Clients')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.title

    def Image_Preview(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/Images/Clients', os.path.basename(str(self.image)))))


