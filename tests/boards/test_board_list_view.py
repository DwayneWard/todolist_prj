import pytest

from goals.models import BoardParticipant, Board


@pytest.mark.django_db
class TestBoardListView:

    def test_no_auth(self, client):
        response = client.get('/goals/board/list')
        assert response.status_code == 403

    def test_no_boards_in_db(self, auth_client):
        response = auth_client.get('/goals/board/list')
        assert response.status_code == 200
        assert response.json() == []

    def test_not_participant(self, user, client, board):
        assert BoardParticipant.objects.filter(user_id=user.id).count() == 0
        assert Board.objects.count() == 1

        client.force_login(user)
        response = client.get('/goals/board/list')
        assert response.status_code == 200
        assert response.json() == []

    @pytest.mark.parametrize("board_participant__role", [
        BoardParticipant.Role.owner,
        BoardParticipant.Role.writer,
        BoardParticipant.Role.reader,
    ], ids=['owner', 'writer', 'reader'])
    def test_board_participant(self, auth_client, board_participant, board_participant__role):
        response = auth_client.get('/goals/board/list')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]['id'] == board_participant.board.id
        assert data[0]['is_deleted'] is False
        assert data[0]['title'] == board_participant.board.title

    @pytest.mark.parametrize('board__is_deleted, boards_count', [
        (True, 0),
        (False, 1)
    ], ids=['deleted', 'not deleted'])
    def test_is_deleted(self, auth_client, board, board_participant, boards_count, board__is_deleted):
        response = auth_client.get('/goals/board/list')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == boards_count
