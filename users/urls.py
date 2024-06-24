from django.urls import path
from .views import UserGroupList, UserGroupDetail, TaskContainerListByUserGroup

urlpatterns = [
    path('user-groups/', UserGroupList.as_view(), name='user-group-list'),
    path('user-groups/<int:pk>/', UserGroupDetail.as_view(), name='user-group-detail'),
    path('user-groups/<int:pk>/task-containers/', TaskContainerListByUserGroup.as_view(), name='taskcontainer-list-by-user-group'),
    path('users/<int:pk>/user-groups/', UserGroupList.as_view(), name='user-group-list')
]
