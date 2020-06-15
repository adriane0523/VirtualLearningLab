from django.shortcuts import render
from zoom.models import Zoom

def class_zoom(request, id_field):
    zoom_result = Zoom.objects.all().filter(courses =(str)(id_field))

    context = {
        "zoom_list": zoom_result,

     
    }

    return render(request, "class_zoom.html", context)