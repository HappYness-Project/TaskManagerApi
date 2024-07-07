from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserGroup
from task.models import TaskContainer
from .serializers import UserGroupSerializer, TaskContainerSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

class UserGroupList(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupListView(generics.ListAPIView):
    serializer_class = UserGroupSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(User, id=user_id)
        return user.user_groups.all()

class TaskContainerListByUserGroup(APIView):
    def get(self, request, pk, format=None):
        task_containers = TaskContainer.objects.filter(user_group_id=pk)
        serializer = TaskContainerSerializer(task_containers, many=True)
        return Response(serializer.data)
    


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

