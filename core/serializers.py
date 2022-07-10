from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_repeat",
        )

    def validate(self, attrs: dict):
        password: str = attrs.get("password")
        password_repeat: str = attrs.pop("password_repeat", None)
        if password != password_repeat:
            raise ValidationError("Пароли не совпадают")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        self.user = user
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Неправильные имя пользователя или пароль")
        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  )
