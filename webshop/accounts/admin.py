from django.contrib import admin
from . import models


class AddressInline(admin.TabularInline):
    model = "UserProfileAdmin"
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'phone_number', 'email', 'age',]
    list_display_links = ['pk',]
    search_fields = ['pk', 'name', 'surname', 'phone_number', 'email',]
    inlines = [AddressInline]