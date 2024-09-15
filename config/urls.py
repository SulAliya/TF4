
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls', namespace='diary')),
    path('users/', include('users.urls', namespace='users'))
]
