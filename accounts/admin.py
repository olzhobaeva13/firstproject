from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    fieldsets = (
        ('System credentials', {'fields': ('username', 'password')}), 
        ('Permissions', {'fields': ('role', )}),
    )

admin.site.register(User, UserAdmin)