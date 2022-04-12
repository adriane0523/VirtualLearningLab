from django.shortcuts import render
from Components.courses.models import Courses
from django.contrib.auth.decorators import login_required

@login_required
def admin(request):
    if request.user.is_superuser:
        courses = Courses.objects.all()
        context = {
            "courses": courses
        }
        

        return render(request, "admin.html", context)
    else:
        return None
