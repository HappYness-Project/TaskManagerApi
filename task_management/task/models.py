import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    class TaskCategory(models.TextChoices):
        GROCERY = 'grocery', _('Grocery')
        TRAVEL = 'travel', _('Travel')
        LEISURE = 'leisure', _('Leisure')
        WORK = 'work', _('Work')

    class Priority(models.TextChoices):
        URGENT = 'urgent', _('Urgent')
        NORMAL = 'normal', _('Normal')
        LOW = 'low', _('Low')

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    task_name = models.CharField(max_length=255)
    task_desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    task_category = models.CharField(max_length=10, choices=TaskCategory.choices, default=TaskCategory.GROCERY)

    def __str__(self):
        return self.task_name

class TaskContainer(models.Model):
    container_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    container_name = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task, related_name='containers')

    def __str__(self):
        return self.container_name
