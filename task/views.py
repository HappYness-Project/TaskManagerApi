from rest_framework import generics
from .models import TaskContainer, Task
from .serializers import TaskContainerSerializer, TaskSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

#Get active user model from django
User = get_user_model()

class TaskContainerListView(generics.ListAPIView):
    queryset = TaskContainer.objects.all()
    serializer_class = TaskContainerSerializer

class TaskContainerDetailView(generics.RetrieveAPIView):
    queryset = TaskContainer.objects.all()
    serializer_class = TaskContainerSerializer

class UserTaskContainerListView(generics.ListAPIView):
    serializer_class = TaskContainerSerializer

    def get_queryset(self):
        user_pk = self.kwargs['user_pk']
        user = get_object_or_404(User, pk=user_pk)
        return TaskContainer.objects.filter(users=user)

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        container_id = self.kwargs['container_id']
        container = get_object_or_404(TaskContainer, container_id=container_id)
        return container.tasks.all()

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'