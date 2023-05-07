from django.contrib import admin
from .models import HumanitasPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HumanitasPost)
class HumanitasPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    search_fields = ['name', 'created_on']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
