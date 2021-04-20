from django.urls import path, include
from API.apps.authentication.views import RegisterUser


app_name = 'API.apps.authentication'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
]