from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_setting = models.OneToOneField('UserSetting', on_delete=models.CASCADE, null=True, blank=True)
    default_user_group_id = models.IntegerField(null=True, blank=True)

class UserSetting(models.Model):
    pass

