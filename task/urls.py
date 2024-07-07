from django.urls import path
from . import views

urlpatterns = [
    path('task-containers/', views.TaskContainerListView.as_view(), name='task-container-list'),
    path('task-containers/<uuid:pk>/', views.TaskContainerDetailView.as_view(), name='task-container-detail'),
    path('users/<int:user_pk>/task-containers/', views.UserTaskContainerListView.as_view(), name='user-task-container-list'),
    path('task-containers/<uuid:pk>/tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<uuid:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<uuid:pk>/toggle-completion/', views.toggle_task_completion, name='task-complete-toggle'),
    path('user-groups/<int:user_group_id>/tasks/', views.UserGroupTasksView.as_view(), name='user-group-tasks'),
]


