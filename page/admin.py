from django.contrib import admin
from .models import Page, PageForm
from slider.models import Slider

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    pass
    # form = PageForm
    # def save_model(self, request, obj, form, change):
    #     super(PageAdmin,self).save_model(request, obj, form, change)
    #     title = request.POST.getlist("title[]")
    #     # print(title)
    #     img_lg_list = request.FILES.getlist("img_lg[]")
    #     # print(img_lg_list)
    #     # print(len(img_lg_list))
    #     img_md_list = request.FILES.getlist("img_md[]")
    #     img_sm_list = request.FILES.getlist("img_sm[]")

    #     text_1_list = request.POST.getlist("text_1[]")
    #     text_2_list = request.POST.getlist("text_2[]")
    #     text_3_list = request.POST.getlist("text_3[]")
        
    #     # print(obj.Slider.filter(project_id=obj.id))
    #     # print(obj.Slider)
    #     for i, _ in enumerate(range(len(img_lg_list))):
    #         if (title[i] == '' or img_lg_list[i] == '' or img_md_list[i] == '' or img_sm_list[i] == '' or text_1_list[i] == '' or text_2_list[i] == '' or text_3_list[i] == ''):
    #             print("Wrong")
    #         else:
    #             for i, _ in enumerate(range(len(img_lg_list))):
    #                 print("Correct")
    #                 # sl_id = obj.Slider.create(Title=title[i], Image_Large=img_lg_list[i] , Image_Medium=img_md_list[i] ,Image_Small=img_sm_list[i] ,Text_1=text_1_list[i], Text_2=text_2_list[i], Text_3=text_3_list[i])
    #                 obj.Slider.create(Title=title[i], Image_Large=img_lg_list[i] , Image_Medium=img_md_list[i] ,Image_Small=img_sm_list[i] ,Text_1=text_1_list[i], Text_2=text_2_list[i], Text_3=text_3_list[i])
                    # sl_id.save()
                    # obj.Slider.add(sl_id)

                    # form.save_m2m()
                    # print(form)
                    # print(sl_id.id)
                    # obj.save()
                    # print(obj.id)
                    # print(form)
                    # print('--------------')
                    # print(request)
                    # obj.Slider = sl_id
                    # form.obj.Slider.add(sl_id)
                    # obj.save()
                    # form.save_m2m()
                    # obj.Slider.add(sl_id)
                    # print(obj.objects.all())
                    # p = Page.objects.filter(id=obj.id).first()
                    # s = Slider.objects.filter(id=sl_id.id).first()
                    # p.Slider.add(sl_id)
                    # p.save()
                    # print('--------------')
                    # print(p)
                    # print(s)
                    # print('--------------')
                    # try:
                    #     p.Slider.add(s)
                    #     print('Done')
                    # except:
                    #     print("Not Done")
                    # obj.Slider.add(sl_id)
                    # p.Slider = s
                    # p.save()
                    # obj.Slider.save()
                    # obj.Slider.through.objects.create(page_id=obj.id, slider_id=str(sl_id.id))

        # for afile in request.FILES.getlist('img_lg[]'):
        #     print('-----------------------------')
        #     print(afile)
        #     print('-----------------------------')
        #     obj.Slider.create(Image_Large=afile, Title='pop')
        

# admin.site.register(Page, PageAdmin)
admin.site.register(Page)
