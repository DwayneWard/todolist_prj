from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя. Заменяет стандартного пользователя Django
    """
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
