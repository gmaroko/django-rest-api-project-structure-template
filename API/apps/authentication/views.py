from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from API.apps.authentication.serializers import UserRegisterSerializer

# Create your views here.
from logging import warning

class RegisterUser(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        msg = {
            "sucess": "User registered successfully"
        }
        return Response(msg, status = status.HTTP_201_CREATED)