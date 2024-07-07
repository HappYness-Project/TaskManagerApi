# from rest_framework import serializers
# from users.models import UserGroup, UserSetting
# from task.serializers import TaskContainerSerializer
# from .models import User 

# class UserSettingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserSetting
#         fields = '__all__'

# class UserGroupSerializer(serializers.ModelSerializer):
#     task_containers = TaskContainerSerializer(many=True, read_only=True)

#     class Meta:
#         model = UserGroup
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     user_setting = UserSettingSerializer()
#     user_groups = UserGroupSerializer(many=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'user_setting', 'user_groups']
