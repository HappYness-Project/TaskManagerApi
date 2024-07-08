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

    def test_user_group_list(self):
        response = self.client.get(reverse('user-group-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['group_name'], self.user_group.group_name)

    def test_user_group_detail(self):
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

    def test_user_detail(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

class TaskContainerListByUserGroupTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_group = UserGroup.objects.create(group_name="Test Group", group_type="Test Type")
        self.task_container = TaskContainer.objects.create(container_name="Test Container", user_group=self.user_group)

    def test_task_container_list_by_user_group(self):
        response = self.client.get(reverse('taskcontainer-list-by-user-group', kwargs={'pk': self.user_group.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['container_name'], self.task_container.container_name)
