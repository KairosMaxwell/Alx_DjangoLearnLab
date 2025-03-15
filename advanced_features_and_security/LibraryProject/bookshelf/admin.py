from django.contrib import admin

from .models import Book, CustomUser, CustomUserManager


class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author')

'''
"list_filter", "author", "publication_year"
'''
# Register your models here.
# admin.site.register(Book)
admin.ModelAdmin(Book,BookAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    # Define fields for filtering in the admin sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    # Allow searching for users by specific fields
    search_fields = ('email', 'first_name', 'last_name')
    # Read-only fields for display purposes
    readonly_fields = ('last_login', 'date_joined')
    # Specify fieldsets for creating and editing users
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Fields for creating new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    # Specify ordering of displayed records
    ordering = ('email',)

admin.site.register(CustomUser,CustomUserAdmin)