from django.contrib import admin
from .models import HumanitasPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HumanitasPost)
class HumanitasPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
