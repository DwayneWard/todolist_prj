import pytest
from rest_framework import status

from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
def test_retrieve_category(auth_client, goal_category, board_participant):
    response = auth_client.get(f"/goals/goal_category/{goal_category.id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == GoalCategorySerializer(goal_category).data


@pytest.mark.django_db
def test_unauthorized(client, goal_category):

    response = client.get(f"/goals/goal_category/{goal_category.pk}")

    assert response.status_code == status.HTTP_403_FORBIDDEN
