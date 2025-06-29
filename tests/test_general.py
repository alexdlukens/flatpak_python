import datetime
from typing import Generator

import pytest
from openapi_client.models.app_of_the_day import AppOfTheDay

from flatpak_python.client import FlatpakPythonClient


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


def test_app_of_the_day(client_fixture: FlatpakPythonClient):
    """
    Test the app of the day method of the FlatpakPythonClient.
    """
    app_of_the_day = client_fixture.app_picks_api.get_app_of_the_day()
    assert app_of_the_day is not None, "Expected app of the day to be returned."

    assert isinstance(app_of_the_day, AppOfTheDay)

    app_of_the_day = client_fixture.app_picks_api.get_app_of_the_day("2023-10-01")
    assert app_of_the_day is not None, (
        "Expected app of the day for specific date to be returned."
    )
    assert isinstance(app_of_the_day, AppOfTheDay)
    assert app_of_the_day.day == datetime.date(2023, 10, 1)
    assert app_of_the_day.app_id == "tv.kodi.Kodi"
