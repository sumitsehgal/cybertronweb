from django.contrib import admin
from .models import Project, Category, Skill, Image
from django.template.defaultfilters import truncatechars
# Register your models here.


admin.site.register(Category)
admin.site.register(Skill)

class ImageAdmin(admin.ModelAdmin):                     # This would not show the `Images` Panel in the Admin List, but it can
    get_model_perms = lambda self, request: {}          # be Edited from the Projects Objects.

admin.site.register(Image, ImageAdmin)


class ProjectAdmin(admin.ModelAdmin):

    def category(self, obj):
        # print(obj.categories.all())
        return ", ".join(c.title for c in obj.categories.all())
    category.short_description = "categories"

    def skill(self, obj):
        return ", ".join(s.title for s in obj.skills.all())
    skill.short_description = "skills"

    def desc(self, obj):
        return truncatechars(obj.description, 10)
    desc.short_description = "description"

    list_display = ['title', 'desc', 'skill', 'category']
    search_fields = ['title', 'description', 'skills__title']

    
admin.site.register(Project, ProjectAdmin)

