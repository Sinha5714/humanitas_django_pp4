# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal:
from .models import HumanitasPost, Comment


@admin.register(HumanitasPost)
class HumanitasPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created_on']
