from django.contrib import admin
from .models import HumanitasPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HumanitasPost)
class HumanitasPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
