from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserGroup, UserSetting

class UserInline(admin.TabularInline):
    model = User.user_groups.through  # This allows access to the many-to-many relationship
    extra = 1  # Number of empty forms to display

class UserGroupAdmin(admin.ModelAdmin):
    inlines = [UserInline]
    list_display = ('group_name', 'group_type')
    search_fields = ('group_name', 'group_type')

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ('user_groups',)  # Allow easy filtering of user groups in the user admin

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(UserSetting)
