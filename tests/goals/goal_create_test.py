import pytest

from tests.factories import GoalFactory

#
# @pytest.mark.django_db
# def test_goal_create(client, category):
#     goal = GoalFactory.create()
#
#     response = client.post('goals/goal/create',
#                            {
#                                "category": category.id,
#                                'title': 'test_goal',
#                                'description': 'test_description',
#                                'due_date': "2022-08-05",
#                                'status': 1,
#                                'priority': 1,
#                            },
#                            content_type='application/json',
#                            )
#
#
#     expected_responce = {
#         'id': 1,
#         'title'
#     }
