from django.urls import path
from API.apps.authentication.views import UserLogin

app_name = "authentication"

urlpatterns = [
    # endpoint routes
    path('login/', UserLogin.as_view(), name='user_login'),
]
