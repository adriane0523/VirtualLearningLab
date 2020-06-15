from django.shortcuts import render
from courses.models import Courses
from django.contrib.auth.decorators import login_required

@login_required
def course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    
    }
    

    return render(request, "course.html", context)

