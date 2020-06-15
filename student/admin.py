from django.contrib import admin
from student.models import Post, WelcomePage, Connect, ReadingMaterial

class PostAdmin(admin.ModelAdmin):
    pass


class WelcomePageAdmin(admin.ModelAdmin):
    pass

class ConnectPageAdmin(admin.ModelAdmin):
    pass

class ReadingMaterialAdmin(admin.ModelAdmin):
    pass



admin.site.register(ReadingMaterial, ReadingMaterialAdmin)
admin.site.register(Connect, ConnectPageAdmin )
admin.site.register(Post, PostAdmin)
admin.site.register(WelcomePage, WelcomePageAdmin)