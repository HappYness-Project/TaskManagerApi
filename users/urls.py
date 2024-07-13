from django.urls import path
from .views import UserGroupList, UserGroupListByUser, UserGroupDetail, TaskContainerListByUserGroup, UserDetail

urlpatterns = [
    path('user-groups/', UserGroupList.as_view(), name='user-group-list'),
    path('user-groups/<int:pk>/', UserGroupDetail.as_view(), name='user-group-detail'),
    path('user-groups/<int:pk>/task-containers/', TaskContainerListByUserGroup.as_view(), name='taskcontainer-list-by-user-group'),
    path('users/<int:pk>/user-groups/', UserGroupListByUser.as_view(), name='user-group-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]


