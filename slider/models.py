from django.db import models

# Create your models here.

class Image_Src(models.Model):
    src = models.CharField(max_length=500)

    def __str__(self):
        return self.src