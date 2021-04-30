from django.contrib import admin
from Components.courses.models import Courses
from Components.student.models import Post, WelcomePage, Connect, ReadingMaterial
from Components.quizapp.models import Quiz
# Inlines for Course Model on Admin Site
class WelcomePageStackedInline(admin.StackedInline):
    model = WelcomePage     # Associates model with particular Inline (StackedInline in this case)
    extra = 0               # Changes default number of extra forms rendered

class PostStackedInline(admin.StackedInline):
    model = Post
    extra = 0

class ConnectStackedInline(admin.StackedInline):
    model = Connect
    extra = 0

class ReadingMaterialStackedInline(admin.StackedInline):
    model = ReadingMaterial
    extra = 0

class QuizStackedInline(admin.StackedInline):
    model = Quiz
    extra = 0

# Configuration for Courses on Admin Site
class CoursesAdmin(admin.ModelAdmin):
    model = Courses

    # Links inlines to Course Model on Admin Site (Ordered)
    inlines = [
        WelcomePageStackedInline,
        PostStackedInline,
        ReadingMaterialStackedInline,
        QuizStackedInline,
        ConnectStackedInline,
        ]

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