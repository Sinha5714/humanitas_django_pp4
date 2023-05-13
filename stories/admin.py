from django.contrib import admin
from .models import HumanitasPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HumanitasPost)
class HumanitasPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created_on']
