from rest_framework import generics, status
from .models import TaskContainer, Task
from .serializers import TaskContainerSerializer, TaskSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

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

class TaskDetailView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            container_id = kwargs.get('pk')
            try:
                task_container = TaskContainer.objects.get(container_id=container_id)
            except TaskContainer.DoesNotExist:
                return Response({"error": "TaskContainer not found."}, status=status.HTTP_404_NOT_FOUND)
            
            task = serializer.save()
            task_container.tasks.add(task)
            
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def toggle_task_completion(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    is_completed = request.data.get('is_completed', None)
    if is_completed is not None:
        task.is_completed = not is_completed
        task.save()
        
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({"error": "is_completed field missing in request data"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserGroupTasksView(APIView):
    def get(self, request, user_group_id):
        is_important = request.query_params.get('isImportant')

        if is_important is None:
            return Response({"error": "Query parameter 'isImportant' is required."}, status=status.HTTP_400_BAD_REQUEST)

        is_important = is_important.lower() == 'true'

        task_containers = TaskContainer.objects.filter(user_group_id=user_group_id)
        tasks = Task.objects.filter(containers__in=task_containers, is_important=is_important).distinct()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
