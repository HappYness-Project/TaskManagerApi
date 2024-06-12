from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserGroup
from task.models import TaskContainer
from .serializers import UserGroupSerializer, TaskContainerSerializer

class UserGroupList(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class TaskContainerListByUserGroup(APIView):
    def get(self, request, pk, format=None):
        task_containers = TaskContainer.objects.filter(user_group_id=pk)
        serializer = TaskContainerSerializer(task_containers, many=True)
        return Response(serializer.data)
