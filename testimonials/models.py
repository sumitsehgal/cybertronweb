from django.db import models

class Testimonials(models.Model):
    testimonial = models.TextField()
    client_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.testimonial
