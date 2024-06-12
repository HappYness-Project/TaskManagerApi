from django.db import models
from django.contrib.auth.models import AbstractUser

class UserGroup(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.group_name} ({self.group_type})'

class UserSetting(models.Model):
    # Define any fields for UserSetting if needed
    pass

class User(AbstractUser):
    user_setting = models.OneToOneField(UserSetting, on_delete=models.CASCADE, null=True, blank=True)
    user_group = models.ForeignKey(UserGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name='users', db_column='user_group_id')

    def __str__(self):
        return self.username