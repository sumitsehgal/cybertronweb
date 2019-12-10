from django.shortcuts import render
from django.http import HttpResponse
from Services.models import Services

def index(request):
    Serv = Services.objects.all()
    # print(Serv[1].Icon)
    context = {
        "a": Serv[1].Icon
    }
    # return HttpResponse('Hello')
    return render(request, 'cbt/index.html', context)