from pytest_factoryboy import register

from tests.factories import UserFactory, GoalFactory, GoalCommentFactory, GoalCategoryFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(GoalFactory)
register(GoalCommentFactory)
register(GoalCategoryFactory)
