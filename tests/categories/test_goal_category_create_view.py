from rest_framework import status

import pytest


@pytest.mark.django_db
def test_success(auth_client, goal_category, board_participant):

    data = {
        "title": goal_category.title,
        "board": board_participant.board.pk,
        "user": board_participant.user_id
    }

    response = auth_client.post(
        "/goals/goal_category/create",
        data=data
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == goal_category.title


@pytest.mark.django_db
def test_no_board(auth_client, goal_category, board_participant):
    data = {
        "title": goal_category.title,
        "user": board_participant.user_id
    }

    response = auth_client.post(
        "/goals/goal_category/create",
        data=data
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
