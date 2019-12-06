from django.contrib import admin
from .models import Services

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    # fields = ( 'Title''image_tag','title','description','image','externalURL', )
    fields = ('Icon', 'Icon_Preview', 'Title', 'Heading', 'Sub_Heading', 'Main_Text')
    readonly_fields = ('Icon_Preview', )

admin.site.register(Services, ImageAdmin)
