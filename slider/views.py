from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, FileResponse
from django.template import loader
from .models import Slider
from Services.models import Services
# Create your views here.

def index(request):
    # print(request.method)

    ELements = Slider.objects.all()
    Serv = Services.objects.all()
    print(Serv)
    print(ELements)
    elm = [e for e in ELements]
    print(elm)
    # return render_to_response('', {'Elements': ELements})
    # return HttpResponse(elm)
    # return JsonResponse({'element': elm})
    # return FileResponse(open(elm[0]), 'rb')

    context = {
        'a': elm
        }

    # return HttpResponse(template.render(context, request))
    return render(request, 'slider/index.html', context)