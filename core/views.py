from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from core.models import User
from core.serializers import CreateUserSerializer, LoginSerializer, UserSerializer


class SignUp(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        s: LoginSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = s.validated_data["user"]
        login(request, user=user)
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data)


class ProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
