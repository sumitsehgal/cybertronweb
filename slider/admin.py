from django.contrib import admin
from django.utils.safestring import mark_safe
# import django_admin_thumbnails

# Register your models here.

from .models import Slider

class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    # fields = ( 'Title''image_tag','title','description','image','externalURL', )
    fields = ('Title', 'Image_Large', 'Large_Image_Tag', 'Image_Medium', 'Medium_Image_Tag', 'Image_Small', 'Small_Image_Tag', 'Text_1', 'Text_2', 'Text_3')
    readonly_fields = ('Large_Image_Tag', 'Medium_Image_Tag', 'Small_Image_Tag')


admin.site.register(Slider, ImageAdmin)