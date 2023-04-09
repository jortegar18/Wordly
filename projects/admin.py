from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from .models import MyUser

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'name', 'last_name', 'genre', 'email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('UserCredentials', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name','last_name', 'date_of_birth', 'genre', 'email')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','name','last_name', 'genre', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username','email')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserModelAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
