from django.contrib import admin
from zoom.models import Zoom

class ZoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Zoom, ZoomAdmin )