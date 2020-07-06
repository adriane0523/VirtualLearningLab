from django.contrib import admin
from courses.models import Courses

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    fieldsets = (
        ('Course Name and Description', {
            'fields': ['name', 'description']
        }),
        ('Unique Id (Do not edit)', {
            'fields': ['id']
        }),
    )




admin.site.register(Courses, CoursesAdmin)
