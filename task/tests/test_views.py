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
        self.other_user = User.objects.create_user(username='otheruser', password='password')

        self.client.login(username='testuser', password='password')
        self.task_container = TaskContainer.objects.create(container_name='Test Container', user_group=None)
        self.task = self.task_container.tasks.create(
            task_name='Test Task', priority='urgent', task_category='work'
        )
        
    def test_given_existing_task_container_when_list_is_requested_then_container_is_in_response(self):
        url = reverse('task-container-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if response contains the task container
        response_data = response.json()
        self.assertIsInstance(response_data, list)
        self.assertGreater(len(response_data), 0)
        container_names = [container['container_name'] for container in response_data]
        self.assertIn('Test Container', container_names)

    def test_given_task_container_when_detail_is_requested_then_correct_container_is_returned(self):
        url = reverse('task-container-detail', kwargs={'pk': self.task_container.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['container_name'], 'Test Container')

    def test_should_return_new_task_when_task_is_created_in_task_container(self):
        url = reverse('task-list-create', kwargs={'pk': self.task_container.pk})
        data = {'task_name': 'New Task', 'priority': 'normal', 'task_category': 'leisure'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['task_name'], 'New Task')

    def test_given_existing_task_when_detail_is_requested_then_correct_task_is_returned(self):
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['task_name'], 'Test Task')

    def test_should_update_task_completion_status_when_task_is_toggled(self):
        url = reverse('task-complete-toggle', kwargs={'pk': self.task.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('is_completed', response.json())
