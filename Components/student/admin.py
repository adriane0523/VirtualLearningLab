from django.contrib import admin
from Components.student.models import Post, WelcomePage, Connect, ReadingMaterial
from Components.quizapp.models import Quiz, Question

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'courses')
    list_filter = ['courses']
    fieldsets = (
        ("Title and Description", {
            'fields': ('title', 'description')
        }),
        ('Content', {
            'fields': ('video', 'content')
        }),
         ('Connect lecture to course', {
            'fields': ['courses']
        }),
    )


class WelcomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'courses')
    list_filter = ['courses']
    fieldsets = (
        ("Title", {
            'fields': ['title']
        }),
        ('Content', {
            'fields': [ 'content']
        }),
         ('Connect welcome page to course', {
            'fields': ['courses']
        }),
    )
    

class ConnectPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'courses')
    list_filter = ['courses']
    fieldsets = (
        ("Title", {
            'fields': ['title']
        }),
        ('Content', {
            'fields': [ 'content']
        }),
         ('Connect connect page to course', {
            'fields': ['courses']
        }),
    )

class ReadingMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'courses')
    list_filter = ['courses']
    fieldsets = (
        ("Title", {
            'fields': ['title', 'description']
        }),
        ('Content', {
            'fields': ['link', 'content']
        }),
         ('Connect connect page to course', {
            'fields': ['courses']
        }),
    )

    

#class QuizAdmin(admin.ModelAdmin):
  #  list_display = ('title', 'courses')
   # list_filter = ['courses']
    #fieldsets = (
     #   ("Title", {
      #      'fields': ['title', 'description']
       # }),
        #('Quiz Content', {
         #   'fields': [ 'content']
        #}),
         #('Connect connect page to course', {
          #  'fields': ['courses']
        #}),
    #)
    
admin.site.register(Question)
admin.site.register(Quiz)
#admin.site.register(Quiz, QuizAdmin)
admin.site.register(ReadingMaterial, ReadingMaterialAdmin)
admin.site.register(Connect, ConnectPageAdmin )
admin.site.register(Post, PostAdmin)
admin.site.register(WelcomePage, WelcomePageAdmin)

