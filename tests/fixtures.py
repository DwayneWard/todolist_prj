import pytest

from goals.models import GoalCategory, Goal



@pytest.fixture
@pytest.mark.django_db
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="testuser",
        password="testpassword196"
    )


@pytest.fixture
@pytest.mark.django_db
def logged_in_user(client, user):
    client.login(
        username=user.username, password="testpassword196"
    )
    return user



















@pytest.fixture
# @pytest.mark.django_db
def category_for_user1(user1, board, boardparticipant_user1_owner):
    return GoalCategory.objects.create(title="test category", user=user1, board=board)


@pytest.fixture
# @pytest.mark.django_db
def goal_for_category(category_for_user1):
    return Goal.objects.create(
        title="Test name", category=category_for_user1, due_date='2022-04-05'
    )
