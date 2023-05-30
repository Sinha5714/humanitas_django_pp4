# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
# Internal:
from .models import Profile, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "last_name", "first_name", "email")
    search_fields = ["last_name__startswith", 'email']
    list_filter = ("last_name", )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "email", "created_on")
    search_fields = ['email', 'name']
    list_filter = ("created_on", )
