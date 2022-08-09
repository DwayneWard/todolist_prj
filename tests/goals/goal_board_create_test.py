from datetime import datetime

import pytest

from tests.factories import BoardFactory


@pytest.mark.django_db
def test_board_create(client):
    board = BoardFactory.create()

    response = client.post('/goals/board/create',
                           {
                               "title": "Test",
                           },
                           content_type='application/json',
                           )

    expected_response = {
        'id': 1,
        'created': datetime.now(),
        'updated': datetime.now(),
        'title': "Test",
        'is_deleted': False,
    }

    assert response.status_code == 201
    assert expected_response == response.json()
