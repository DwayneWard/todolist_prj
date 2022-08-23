from django.db import models
from django.utils import timezone

from core.models import User


class DatesModel(models.Model):
    """
    Абстрактный класс для проставления даты в созданном объекте
    """

    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="Дата создания")
    updated = models.DateTimeField(verbose_name="Дата последнего обновления")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Board(DatesModel):
    """
    Модель доски
    """
    title = models.CharField(verbose_name="Название", max_length=255)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)

    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"


class BoardParticipant(DatesModel):
    """
    Модель участника доски.
    Разделение по ролям.
    """
    class Meta:
        unique_together = ("board", "user")
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    class Role(models.IntegerChoices):
        owner = 1, "Владелец"
        writer = 2, "Редактор"
        reader = 3, "Читатель"

    editable_choices = Role.choices
    editable_choices.pop(0)

    board = models.ForeignKey(
        Board,
        verbose_name="Доска",
        on_delete=models.PROTECT,
        related_name="participants",
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.PROTECT,
        related_name="participants",
    )
    role = models.PositiveSmallIntegerField(
        verbose_name="Роль", choices=Role.choices, default=Role.owner
    )


class GoalCategory(DatesModel):
    """
    Модель категории для целей
    """
    board = models.ForeignKey(
        Board,
        verbose_name="Доска",
        on_delete=models.PROTECT,
        related_name="categories"
    )
    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Goal(DatesModel):
    """
    Модель целей.
    Реализован выбор статуса и приоритета
    """
    class Status(models.IntegerChoices):
        to_do = 1, "К выполнению"
        in_progress = 2, "В процессе"
        done = 3, "Выполнено"
        archived = 4, "Архив"

    class Priority(models.IntegerChoices):
        low = 1, "Низкий"
        medium = 2, "Средний"
        high = 3, "Высокий"
        critical = 4, "Критический"

    category = models.ForeignKey(
        GoalCategory,
        verbose_name="Категория",
        on_delete=models.PROTECT
    )

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name="goals",
        on_delete=models.PROTECT,
    )

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=255
    )

    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
        default=None,
    )

    due_date = models.DateField(
        verbose_name="Дата выполнения",
        null=True,
        blank=True,
        default=None,
    )

    status = models.PositiveIntegerField(
        verbose_name="Статус",
        choices=Status.choices,
        default=Status.to_do,
    )

    priority = models.PositiveIntegerField(
        verbose_name="Приоритет",
        choices=Priority.choices,
        default=Priority.medium,
    )

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    def __str__(self):
        return self.title


class GoalComment(DatesModel):
    """
    Модель комментариев к целям
    """
    user = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name='goal_comments',
        on_delete=models.PROTECT,
    )

    goal = models.ForeignKey(
        Goal,
        verbose_name="Цель",
        related_name='goal_comments',
        on_delete=models.PROTECT,
    )

    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
