from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the provided model admin
admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)