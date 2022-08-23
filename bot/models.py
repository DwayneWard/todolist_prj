import random

from django.db import models

CODE_VOCABULARY = "qwertyuasdfghkzxvbnm123456789"


class TgUser(models.Model):
    """
    Модель пользователя для телеграмм-бота
    """
    tg_id = models.BigIntegerField(
        verbose_name="Telegram ID",
        unique=True,
    )
    tg_chat_id = models.BigIntegerField(
        verbose_name='Telegram Chat ID',
        null=True,
        blank=True,
        default=None,
    )
    username = models.CharField(
        max_length=512,
        verbose_name='Telegram username',
        null=True,
        blank=True,
        default=None,
    )
    user = models.ForeignKey(
        "core.User",
        models.PROTECT,
        null=True,
        blank=True,
        default=None,
        verbose_name='Пользователь из приложения',
    )
    verification_code = models.CharField(
        max_length=32, verbose_name="код подтверждения"
    )

    class Meta:
        verbose_name = "Telegram пользователь"
        verbose_name_plural = "Telegram пользователи"

    def set_verification_code(self):
        code = "".join([random.choice(CODE_VOCABULARY) for _ in range(12)])
        self.verification_code = code
