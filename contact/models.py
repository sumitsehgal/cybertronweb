from django.db import models

class Contact(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=18)
    email = models.EmailField()
    website = models.URLField(max_length=200, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()


    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return "Contact Page"