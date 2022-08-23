from rest_framework import status

import pytest


# @pytest.mark.django_db
# def test_success(auth_client, goal, goal_category, board_participant):
#
#     data = {
#         "title": goal.title,
#         "category": goal_category.pk
#     }
#
#     response = auth_client.post(
#         "/goals/goal/create",
#         data=data
#     )
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data["title"] == goal.title


@pytest.mark.django_db
def test_no_category(auth_client, goal, board_participant):
    data = {
        "title": goal.title,
    }

    response = auth_client.post(
        "/goals/goal/create",
        data=data
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
