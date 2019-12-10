from django.contrib import admin

from .models import Clients

class ClientAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'link', 'image', 'Image_Preview')
    readonly_fields = ('Image_Preview', )

admin.site.register(Clients, ClientAdmin)
