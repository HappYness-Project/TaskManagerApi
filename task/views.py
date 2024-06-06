from rest_framework import generics, status
from .models import TaskContainer, Task
from .serializers import TaskContainerSerializer, TaskSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            container_id = request.data.get('container_id')
            try:
                task_container = TaskContainer.objects.get(container_id=container_id)
            except TaskContainer.DoesNotExist:
                return Response({"error": "TaskContainer not found."}, status=status.HTTP_404_NOT_FOUND)
            
            task = serializer.save()
            task_container.tasks.add(task)
            
            headers = self.get_success_headers(serializer.data)
            return Response(status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def toggle_task_completion(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Check if 'is_completed' field is present in the request data
    is_completed = request.data.get('is_completed', None)
    if is_completed is not None:
        # Toggle the value of 'is_completed'
        task.is_completed = not is_completed
        task.save()
        
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({"error": "is_completed field missing in request data"}, status=status.HTTP_400_BAD_REQUEST)