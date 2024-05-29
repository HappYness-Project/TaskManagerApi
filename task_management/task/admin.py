from django.contrib import admin
from .models import Task, TaskContainer

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_category', 'priority', 'is_completed', 'created_date', 'target_date')
    list_filter = ('task_category', 'priority', 'is_completed')

@admin.register(TaskContainer)
class TaskContainerAdmin(admin.ModelAdmin):
    list_display = ('container_name',)
    filter_horizontal = ('tasks',)