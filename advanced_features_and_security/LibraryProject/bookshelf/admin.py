from django.contrib import admin

from .models import Book, CustomUser, CustomUserManager


class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Display these fields in the admin user list
    list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    # Enable filtering options in the admin sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    # Search bar functionality
    search_fields = ('email', 'first_name', 'last_name')
    # Set fields that are read-only
    readonly_fields = ('last_login', 'date_joined')

    # Define fieldsets to group fields in the edit form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Configuration for creating new users in the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    # Specify default ordering of records in the admin user list
    ordering = ('email',)


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import MyModel  # Replace with your model's name

# Step 1: Define groups
groups = {
    "Editors": ["can_edit", "can_create"],
    "Viewers": ["can_view"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
}


# Step 2: Assign permissions
def create_groups_and_permissions():
    content_type = ContentType.objects.get_for_model(MyModel)  # Use your actual model name

    for group_name, permissions in groups.items():
        # Get or create the group
        group, created = Group.objects.get_or_create(name=group_name)

        for perm_name in permissions:
            # Get or create the permission
            permission, perm_created = Permission.objects.get_or_create(
                codename=perm_name,
                name=f"Can {perm_name.replace('_', ' ')} instances of MyModel",
                content_type=content_type,
            )
            # Add the permission to the group
            group.permissions.add(permission)

    print("Groups and permissions created successfully.")


# Call the function
create_groups_and_permissions()

# Register your models here.
# admin.site.register(Book)
admin.ModelAdmin(Book,BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

# admin.ModelAdmin(CustomUserAdmin)