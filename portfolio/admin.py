from django.contrib import admin
from .models import Project, Category, Skill, Image
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
import os  
# from django import forms
from .models import ProjectForm
# Register your models here.

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'thumbnail', 'preview')
    readonly_fields = ('preview', )
admin.site.register(Category, CategoryAdmin)

class SkillAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'thumbnail', 'preview')
    readonly_fields = ('preview', )
admin.site.register(Skill, SkillAdmin)

class ImageAdmin(admin.ModelAdmin):                     # This would not show the `Images` Panel in the Admin List, but it can
    get_model_perms = lambda self, request: {}          # be Edited from the Projects Objects.
admin.site.register(Image, ImageAdmin)

# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 0

class ProjectAdmin(admin.ModelAdmin):

    def category(self, obj):
        # print(obj.categories.all())
        return ", ".join(c.title for c in obj.categories.all())
    category.short_description = "categories"

    def skill(self, obj):
        return ", ".join(s.title for s in obj.skills.all())
    skill.short_description = "skills"

    def desc(self, obj):
        return truncatechars(obj.description, 60)
    desc.short_description = "description"

    def image_thumbnail(self, obj):
        # print(os.path.join('/upload', os.path.basename(str(obj.thumbnail))))
        return mark_safe('<img src="{}" width="50" height="30" />'.format(os.path.join('/Images/upload', os.path.basename(str(obj.thumbnail)))))
    image_thumbnail.short_description = "Thumbnail"

    form = ProjectForm
    # inlines = [ImageInline]

    def save_model(self, request, obj, form, change):
        image_ids = request.POST.getlist("files[]")
        print(image_ids)
        obj.images.filter(project_id=obj.id).exclude(id__in=image_ids).delete()
        super(ProjectAdmin, self).save_model(request, obj, form, change)

        print(request.FILES)
        for afile in request.FILES.getlist('photos_multiple'):
            print('-----------------------------')
            print(afile)
            print('-----------------------------')
            # obj.images.create(file=afile)

    # def image_preview(self, obj):
    #     images = ""
    #     print(obj.images.all())
    #     for image in obj.images.all():
    #         print(image)
    #         images += '<img src="{}" width="50" height="30" />'.format(os.path.join('/Images/upload', os.path.basename(str(image))))
    #     return images

    list_display = ['title', 'image_thumbnail', 'desc', 'skill', 'category']
    search_fields = ['title', 'description', 'skills__title']

    fields = ('title', 'description', 'link', 'thumbnail', 'preview', 'created_at', 'published_at', 'skills', 'categories')
    # readonly_fields = ('preview', 'image_preview')
    readonly_fields = ('preview',)
admin.site.register(Project, ProjectAdmin)

