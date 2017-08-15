import pytest
from rest_framework.test import APIClient

from core.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        'username': '...',
        'password': '...',
        'email': '...',
        'first_name': '...',
        'last_name': '...',
        'date_of_birth': '...',
        'address': '...',
    }


def test_not_confirmed_after_registration(api_client, user_data):
    """Verifies that the user is not confirmed right after the registration.
    """
    # WHEN a user registers
    response = api_client.post('/api/register', data=user_data)
    assert response == 200
    user = User.objects.get(id=response['id'])

    # THEN his is_active should be set to False
    assert user.is_active == False
