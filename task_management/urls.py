from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),  # Include URLs from the 'task' app
    path('', include('users.urls')),
]
