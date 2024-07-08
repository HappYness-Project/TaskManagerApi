from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from task.models import TaskContainer, Task
from task.serializers import TaskContainerSerializer, TaskSerializer

User = get_user_model()

class TaskViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.task_container = TaskContainer.objects.create(container_name='Test Container', user_group=None)
        self.task = self.task_container.tasks.create(
            task_name='Test Task', priority='urgent', task_category='work'
        )

    def test_task_container_list(self):
        url = reverse('task-container-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_container_detail(self):
        url = reverse('task-container-detail', kwargs={'pk': self.task_container.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_task_container_list(self):
        url = reverse('user-task-container-list', kwargs={'user_pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_list_create(self):
        url = reverse('task-list-create', kwargs={'pk': self.task_container.pk})
        data = {'task_name': 'New Task', 'priority': 'normal', 'task_category': 'leisure'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('task_name', response.data)

    def test_task_detail(self):
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_toggle_task_completion(self):
        url = reverse('task-complete-toggle', kwargs={'pk': self.task.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('is_completed', response.data)

    def test_user_group_tasks_view(self):
        # Replace with an existing user group id
        user_group_id = 1  # Replace with an actual existing user group id
        url = reverse('user-group-tasks', kwargs={'user_group_id': user_group_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
