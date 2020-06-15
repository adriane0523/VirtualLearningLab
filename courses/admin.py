from django.contrib import admin
from courses.models import Courses

class CoursesAdmin(admin.ModelAdmin):
    pass




admin.site.register(Courses, CoursesAdmin)

