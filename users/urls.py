from django.urls import path
from .views import UserGroupList, UserGroupDetail, TaskContainerListByUserGroup

urlpatterns = [
    path('api/user-groups/', UserGroupList.as_view(), name='user-group-list'),
    path('api/user-groups/<int:pk>/', UserGroupDetail.as_view(), name='user-group-detail'),
    path('api/user-groups/<int:pk>/task-containers/', TaskContainerListByUserGroup.as_view(), name='taskcontainer-list-by-user-group'),
]
