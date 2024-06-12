from rest_framework import serializers
from users.models import UserGroup
from task.serializers import TaskContainerSerializer

class UserGroupSerializer(serializers.ModelSerializer):
    task_containers = TaskContainerSerializer(many=True, read_only=True)

    class Meta:
        model = UserGroup
        fields = '__all__'