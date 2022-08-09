from http import HTTPStatus

import pytest

from goals.serializers import GoalSerializer
from tests.factories import GoalFactory, UserFactory


@pytest.mark.django_db
def test_with_authenticated_client(client, django_user_model):
    username = "user1"
    password = "bar"
    # user = django_user_model.objects.create_user(username=username, password=password)
    # # Use this:
    # client.force_login(user)
    # Or this:
    client.login(username=username, password=password)
    response = client.get('/goals/goal/list')

    assert response.status_code == HTTPStatus.OK
# def test_get_all_by_owner(client, logged_in_user, goals_for_category):
#     goal_1, goal_2 = goals_for_category
#
#     expected_response = [
#         GoalSerializer(goal_1).data,
#         GoalSerializer(goal_2).data,
#     ]
#     response = client.get("/goals/goal/list")
#
#     assert response.status_code == HTTPStatus.OK
#     assert sorted(response.json(), key=lambda x: x["id"]) == expected_response

#
@pytest.mark.django_db
def test_goals_list(client, logged_in_user):
    goals_factory = GoalFactory.create_batch(5)

    client.login(username=logged_in_user.username, password=logged_in_user.password)
    # login = client.post('/core/login',
    #                     {'username': user.username, "password": user.password},
    #                     content_type='application/json'
    #                     )

    response = client.get('/goals/goal/list')

    goals = []
    for goal in goals_factory:
        goals.append(
            {
                'id': goal.id,
                'created': goal.created,
                'updated': goal.updated,
                'title': goal.title,
                'description': goal.description,
                'due_date': goal.due_date,
                'status': goal.status,
                'priority': goal.priority,
                'category_id': goal.category_id,
                'user_id': goal.user_id,
            }
        )

    expected_response = {
        'items': goals,
        'num_pages': 1,
        'total': 5,
    }

    # assert login.status_code == 200
    assert response.status_code == 200
    assert response.json() == expected_response
