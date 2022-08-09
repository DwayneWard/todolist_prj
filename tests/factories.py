import factory

from core.models import User
from goals.models import Goal, GoalCategory, GoalComment, Board


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker('name')


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    board = factory.SubFactory(BoardFactory)
    title = factory.Faker('name')
    user = factory.SubFactory(UserFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    category = factory.SubFactory(GoalCategoryFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.Faker('name')


class GoalCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalComment

    user = factory.SubFactory(UserFactory)
    goal = factory.SubFactory(GoalFactory)
    text = factory.Faker("name")
