from django.contrib import admin
from django.contrib.auth.models import User
from . import models


class AddressInline(admin.TabularInline):
    model = models.Address
    extra = 1

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'balance', 'phone_number', 'email', 'age',]
    list_display_links = ['pk', 'balance',]
    search_fields = ['pk', 'name', 'surname', 'phone_number', 'email', 'balance',]
    inlines = [AddressInline]

@admin.register(models.Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'profile', 'value']
    list_display_links = ['pk', 'profile']
    search_fields = ['pk', 'profile',]

@admin.register(models.Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ['pk', 'profile', 'post_index', 'country', 'region', 'city']
    list_display_links = ['pk']
    search_fields = ['pk', 'country', 'region', 'city']