from django.contrib.auth.views import LoginView
from django.urls import path
from users.apps import UsersConfig
from diary.views import home

app_name = UsersConfig.name

urlpatterns = [

    path('login/', LoginView.as_view(template_name='login.html'))
]
