from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import CreateUserSerializer


class SignUp(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer
