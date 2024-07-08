from django.db import models
import uuid
from django.contrib.auth import get_user_model
from users.models import UserGroup
from django.utils import timezone

class TaskCategory(models.TextChoices):
    GROCERY = 'grocery', 'Grocery'
    TRAVEL = 'travel', 'Travel'
    LEISURE = 'leisure', 'Leisure'
    WORK = 'work', 'Work'

class Priority(models.TextChoices):
    URGENT = 'urgent', 'Urgent'
    NORMAL = 'normal', 'Normal'
    LOW = 'low', 'Low'

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.CharField(max_length=255)
    task_desc = models.TextField(null=True, blank=True, max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=Priority.choices)
    task_category = models.CharField(max_length=10, choices=TaskCategory.choices)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

class TaskContainer(models.Model):
    container_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    container_name = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task, related_name='containers')
    user_group = models.ForeignKey(UserGroup, related_name='containers', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.container_name

    @classmethod
    def from_json(cls, json_data):
        tasks = [Task.objects.get(task_id=task_id) for task_id in json_data['tasks']]
        return cls(container_name=json_data['container_name'], tasks=tasks)
