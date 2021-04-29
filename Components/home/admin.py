from django.contrib import admin
from .models import HomeNotification

# Register your models here.
class HomeNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'active')
    list_filter = ['message', 'active']
    fieldsets = (
        ('Notification content', {
            'fields': ['message']
        }),
        ('Show on HomePage', {
            'fields': ['active']
        }),
    )

admin.site.register(HomeNotification, HomeNotificationAdmin)