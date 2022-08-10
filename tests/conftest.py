import pytest
from pytest_factoryboy import register

from tests.factories import UserFactory, BoardFactory, BoardParticipantFactory

register(UserFactory)
register(BoardFactory)
register(BoardParticipantFactory)


@pytest.fixture
@pytest.mark.django_db
def auth_client(client, user):
    client.force_login(user)
    return client
