from django.contrib import admin
from .models import User


class User_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(User, User_Admin)