from django.shortcuts import render
from django.http import HttpResponse
from Services.models import Services
from slider.models import Slider
from page.models import Page
from portfolio.models import Project

def index(request):
    # slider = Slider.objects.all()
    # slider = Slider.objects.filter(Title="Slide 1")
    page = Page.objects.filter(Title="Index")
    print(page)
    # print(page.first().Slider.first().Image_Medium)
    # print(page.first().Slider.first().Image_Medium)
    project = Project.objects.all()[:3]
    print(project)
    # print('-------------------')
    # print(project)
    # print('-------------------')

    
    return render(request, 'cbt/index.html', {"a": page, "p": project})













    # def index(request):
    # slider = Slider.objects.all()
    # slider = Slider.objects.filter(Title="Slide 1")
    # page = Page.objects.filter(Title="Testing")
    # print(Serv[1].Icon)
    # print(page.first().Slider.first().Image_Large)
    # for s in slider:
    #     for d in s:
    #         print('----------')
    #         print(d)
    #         print('----------')

    #     break
    # slider = slider[0]
    # context = {
    #     "a": slider
    # }
    # a = page
    # return HttpResponse('Hello')
    # return render(request, 'cbt/index.html', {"a": page})