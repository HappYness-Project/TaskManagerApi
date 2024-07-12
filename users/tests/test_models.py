from django.test import TestCase
from django.utils import timezone
from users.models import User, UserGroup, UserSetting
from django.contrib.auth import get_user_model

User = get_user_model()

class UserGroupModelTest(TestCase):

    def create_user_group(self, group_name="Test Group", group_type="Test Type"):
        return UserGroup.objects.create(group_name=group_name, group_type=group_type)

    def test_given_valid_data_when_user_group_is_created_then_user_group_instance_should_be_returned(self):
        user_group = self.create_user_group()
        self.assertTrue(isinstance(user_group, UserGroup))
        self.assertEqual(user_group.__str__(), f'{user_group.group_name} ({user_group.group_type})')


class UserSettingModelTest(TestCase):

    def create_user_setting(self, default_group_id=1):
        return UserSetting.objects.create(default_group_id=default_group_id)

    def test_given_valid_data_when_user_setting_is_created_then_user_setting_instance_should_be_returned(self):
        user_setting = self.create_user_setting()
        self.assertTrue(isinstance(user_setting, UserSetting))
        self.assertEqual(user_setting.default_group_id, 1)


class UserModelTest(TestCase):

    def create_user(self, username="testuser", email="testuser@example.com", password="password123"):
        user_setting = UserSetting.objects.create(default_group_id=1)
        user = User.objects.create_user(username=username, email=email, password=password, user_setting=user_setting)
        return user

    def test_given_valid_data_when_user_is_created_then_user_instance_should_be_returned(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("password123"))
        self.assertEqual(user.__str__(), user.username)

    def test_given_user_and_user_group_when_user_is_added_to_group_then_user_should_be_in_group(self):
        user = self.create_user()
        user_group = UserGroup.objects.create(group_name="Test Group", group_type="Test Type")
        user.user_groups.add(user_group)
        self.assertIn(user_group, user.user_groups.all())
        self.assertEqual(user.user_groups.count(), 1)
        self.assertEqual(user_group.group_users.count(), 1)
