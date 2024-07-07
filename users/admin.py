from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserGroup, UserSetting

admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(UserSetting)