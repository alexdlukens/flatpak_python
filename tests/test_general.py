import pytest
from flatpak_python.client import FlatpakPythonClient
from typing import Generator


@pytest.fixture
def client_fixture() -> Generator[FlatpakPythonClient, None, None]:
    client = FlatpakPythonClient()
    client.init_apis()
    yield client


def test_ping(client_fixture: FlatpakPythonClient):
    """
    Test the ping method of the FlatpakPythonClient.
    """
    response = client_fixture.ping()
    assert response is not None
    assert response.status == "OK", (
        "Expected status to be 'OK' from the health check response."
    )
