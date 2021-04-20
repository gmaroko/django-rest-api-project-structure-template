import pytest
import rest_framework

pytest_plugins = (
    'API.tests.fixtures.user',
    'API.tests.fixtures.business',
)

@pytest.fixture(scope='function')
def client():
    """
    put, get 
    client = APIClient()
    res = client.get(url, context)
    """
    from rest_framework.test import APIClient
    return APIClient()
