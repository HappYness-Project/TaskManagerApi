from rest_framework import serializers
from users.models import UserGroup, UserSetting
from task.serializers import TaskContainerSerializer
from .models import User 


class BasicUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['id', 'group_name', 'group_type']

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user_setting = UserSettingSerializer()
    user_groups = serializers.StringRelatedField(many=True)  # Avoid using UserGroupSerializer to prevent circular reference

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_setting', 'user_groups']

class UserGroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True, source='group_users')

    class Meta:
        model = UserGroup
        fields = ['id', 'group_name', 'group_type', 'users']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data('first_name'),
            last_name=validated_data('last_name'),
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user