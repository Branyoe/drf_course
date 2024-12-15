from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser, Movie


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ("title", "genre", "year", "created_date", "updated_date")
    list_display = ("title", "genre", "year", "created_date", "updated_date")
    search_fields = ("title", "genre", "year")
    readonly_fields = ("created_date", "updated_date")
    list_filter = ("genre", "year")
    ordering = ("-created_date", "-updated_date", "title", "genre", "year")
    