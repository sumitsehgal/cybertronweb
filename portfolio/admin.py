from django.contrib import admin

from .models import Project, Category, Skill, Image
# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Image)
