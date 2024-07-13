from django.test import TestCase
from task.models import Task, TaskContainer, TaskCategory, Priority
from users.models import UserGroup
from django.utils import timezone
import uuid

class TaskModelTest(TestCase):
    def create_task(self, task_name="Test Task"):
        return Task.objects.create(
            task_id=uuid.uuid4(),
            task_name=task_name,
            task_desc="This is a test task description.",
            created_date=timezone.now(),
            target_date=timezone.now() + timezone.timedelta(days=1),
            is_completed=False,
            priority=Priority.NORMAL,
            task_category=TaskCategory.WORK,
            is_important=False
        )

    def test_given_valid_data_when_task_is_created_then_task_instance_should_be_returned(self):
        task = self.create_task()
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), task.task_name)

class TaskContainerModelTest(TestCase):

    def create_task_container(self, container_name="Test Container"):
        user_group = UserGroup.objects.create(group_name="Test Group", group_type="Test Type")
        return TaskContainer.objects.create(container_name=container_name, user_group=user_group)

    def test_given_valid_data_when_task_container_is_created_then_task_container_instance_should_be_returned(self):
        task_container = self.create_task_container()
        self.assertTrue(isinstance(task_container, TaskContainer))
        self.assertEqual(task_container.__str__(), task_container.container_name)

    def test_given_tasks_when_added_to_task_container_then_task_container_should_contain_those_tasks(self):
        task_container = self.create_task_container()
        task1 = Task.objects.create(
            task_id=uuid.uuid4(),
            task_name="Task 1",
            task_desc="Description for task 1.",
            created_date=timezone.now(),
            target_date=timezone.now() + timezone.timedelta(days=1),
            is_completed=False,
            priority=Priority.NORMAL,
            task_category=TaskCategory.WORK,
            is_important=False
        )
        task2 = Task.objects.create(
            task_id=uuid.uuid4(),
            task_name="Task 2",
            task_desc="Description for task 2.",
            created_date=timezone.now(),
            target_date=timezone.now() + timezone.timedelta(days=2),
            is_completed=False,
            priority=Priority.LOW,
            task_category=TaskCategory.LEISURE,
            is_important=True
        )
        task_container.tasks.set([task1, task2])
        self.assertEqual(task_container.tasks.count(), 2)
        self.assertIn(task1, task_container.tasks.all())
        self.assertIn(task2, task_container.tasks.all())
