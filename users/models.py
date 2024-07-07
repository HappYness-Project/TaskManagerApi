from django.db import models
from django.contrib.auth.models import AbstractUser

class UserGroup(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.group_name} ({self.group_type})'

class UserSetting(models.Model):
    default_group_id = models.IntegerField(null=True, blank=True)

class User(AbstractUser):
    user_setting = models.OneToOneField(UserSetting, on_delete=models.CASCADE, null=True)
    user_groups = models.ManyToManyField(UserGroup, related_name='group_users')  # Unique related_name for User

    def __str__(self):
        return self.username
