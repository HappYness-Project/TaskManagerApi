from django.urls import path
from . import views

urlpatterns = [
    path('api/task-containers/', views.TaskContainerListView.as_view(), name='task-container-list'),
    path('api/task-containers/<uuid:container_id>/', views.TaskContainerDetailView.as_view(), name='task-container-detail'),
    path('api/users/<int:user_pk>/task-containers/', views.UserTaskContainerListView.as_view(), name='user-task-container-list'),
    path('api/task-containers/<uuid:container_id>/tasks/', views.TaskListView.as_view(), name='task-list'),
    path('api/tasks/<uuid:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('api/tasks/delete/<uuid:pk>/',views.TaskDeleteView.as_view(), name='task-delete'),
]
