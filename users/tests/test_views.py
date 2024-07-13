from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User, UserGroup, UserSetting
from task.models import TaskContainer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserGroupViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_group_data = {'group_name': 'Test Group', 'group_type': 'Test Type'}
        self.user_group = UserGroup.objects.create(**self.user_group_data)

    def test_given_existing_user_group_when_list_is_requested_then_user_group_is_in_response(self):
        response = self.client.get(reverse('user-group-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['group_name'], self.user_group.group_name)

    def test_given_existing_user_group_when_detail_is_requested_then_correct_user_group_is_returned(self):
        response = self.client.get(reverse('user-group-detail', kwargs={'pk': self.user_group.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['group_name'], self.user_group.group_name)

class UserDetailTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_setting = UserSetting.objects.create(default_group_id=1)
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'user_setting': self.user_setting
        }
        self.user = User.objects.create_user(**self.user_data)
        self.user.user_groups.add(UserGroup.objects.create(group_name="Test Group", group_type="Test Type"))

    def test_given_existing_user_when_detail_is_requested_then_correct_user_is_returned(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
