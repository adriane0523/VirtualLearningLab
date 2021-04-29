from django.contrib import admin
from .models import *
 
# Register your models here.

class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('courses', 'title', 'created_on')
    list_filter = ['courses']
    fieldsets = (
        ('Connect Discussion Board to Course', {
            'fields': ['courses']
        }),
        ("Title", {
            'fields': ['title', 'created_by']
        }),
        ('Content', {
            'fields': [ 'content']
        }),
         
    )
    search_fields = ['title', 'content', 'created_on']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('parent_discussion', 'created_by', 'content', 'created_on', 'num_vote_up')
    list_filter = ['created_on']
    fieldsets = (
        ("Parent Discussion", {
            'fields': ['parent_discussion']
        }),
        ('Author', {
            'fields': ['created_by']
        }),
        ('Comment Content', {
            'fields': ['content']
        }),
    )
    search_fields = ['created_by', 'content', 'created_on']

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'created_by', 'reply', 'created_on')
    list_filter = ['created_on']
    fieldsets = (
        ("Parent Comment", {
            'fields': ['comment']
        }),
        ('Author', {
            'fields': ['created_by']
        }),
        ('Reply Content', {
            'fields': ['reply']
        }),
    )
    search_fields = ['created_by', 'reply', 'created_on']

admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)