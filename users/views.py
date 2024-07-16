from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserGroup
from task.models import TaskContainer
from .serializers import UserGroupSerializer, TaskContainerSerializer, UserSerializer, UserCreateSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserGroupList(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupListByUser(generics.ListAPIView):
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

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddUserToGroupView(APIView):
    def post(self, request, user_group_id):
        user_id = request.data.get('user_id')

        # Validate user_id is provided
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, id=user_id)
        user_group = get_object_or_404(UserGroup, id=user_group_id)

        # Check if the user is already in the group
        if user in user_group.group_users.all():
            return Response({"detail": "User is already a member of the group."}, status=status.HTTP_200_OK)

        user_group.group_users.add(user)
        user_group.save()

        return Response({"detail": "User added to group successfully."}, status=status.HTTP_201_CREATED)