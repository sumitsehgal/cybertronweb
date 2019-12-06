from django.db import models
# from django.utils.html import escape
import os
from django.utils.safestring import mark_safe

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Slider(models.Model):
    # These are the 3 Image Field Variables
    Title = models.CharField(max_length=100)
    Image_Large = models.ImageField(upload_to='static/Images/Slider')
    Image_Medium = models.ImageField(upload_to='static/Images/Slider')
    Image_Small = models.ImageField(upload_to='static/Images/Slider')

    # These are the 3 Text Field Variables
    Text_1 = models.CharField(max_length=100)
    Text_2 = models.CharField(max_length=100)
    Text_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.Title

    # def url(self):
    #     print(BASE_DIR)
    #     print(os.path.join('/Images/static/Images/Slider', os.path.basename(str(self.Image_Large))))
    #     return os.path.join('/Images/static/Images/Slider', os.path.basename(str(self.Image_Large)))

    def Large_Image_Tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/static/Images/Slider', os.path.basename(str(self.Image_Large)))))
    
    def Medium_Image_Tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/static/Images/Slider', os.path.basename(str(self.Image_Medium)))))
    
    def Small_Image_Tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(os.path.join('/Images/static/Images/Slider', os.path.basename(str(self.Image_Small)))))
    
    
    Large_Image_Tag.short_description = 'Large Image Preview'
    Medium_Image_Tag.short_description = 'Medium Image Preview'
    Small_Image_Tag.short_description = 'Short Image Preview'

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'


    # http://localhost:8000/Images/static/Images/Slider/Flowers.jpeg  
