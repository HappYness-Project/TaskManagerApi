from django.urls import path
from .views import UserGroupList, UserGroupDetail, TaskContainerListByUserGroup

urlpatterns = [
    path('api/usergroups/', UserGroupList.as_view(), name='usergroup-list'),
    path('api/usergroups/<int:pk>/', UserGroupDetail.as_view(), name='usergroup-detail'),
    path('api/usergroups/<int:pk>/task-containers/', TaskContainerListByUserGroup.as_view(), name='taskcontainer-list-by-usergroup'),
]
