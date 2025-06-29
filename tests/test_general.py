import datetime
from typing import Generator

import pytest
from flathub_python_api.models.app_of_the_day import AppOfTheDay
from flathub_python_api.models.app_of_the_week import AppOfTheWeek
from flathub_python_api.models.apps_of_the_week import AppsOfTheWeek

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


def test_app_of_the_week(client_fixture: FlatpakPythonClient):
    """
    Test the app of the week method of the FlatpakPythonClient.
    """
    apps_of_the_week = client_fixture.app_picks_api.get_apps_of_the_week()
    assert apps_of_the_week is not None, "Expected apps of the week to be returned."

    assert isinstance(apps_of_the_week, AppsOfTheWeek)

    apps_of_the_week = client_fixture.app_picks_api.get_apps_of_the_week("2025-01-01")
    assert apps_of_the_week is not None, (
        "Expected apps of the week for specific date to be returned."
    )
    assert isinstance(apps_of_the_week, AppsOfTheWeek)
    assert apps_of_the_week.apps is not None, (
        "Expected apps of the week to contain a list of AppOfTheWeek objects."
    )
    assert len(apps_of_the_week.apps) > 0, (
        "Expected apps of the week to contain at least one app."
    )
    assert all(isinstance(app, AppOfTheWeek) for app in apps_of_the_week.apps), (
        "Expected all items in apps of the week to be instances of AppOfTheWeek."
    )

    assert apps_of_the_week.apps[0].app_id == "de.schmidhuberj.Flare", (
        "Expected the first app of the week to be 'de.schmidhuberj.Flare'."
    )
