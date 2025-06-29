import datetime
from typing import Optional

import flathub_python_api.api as flatpak_apis
from flathub_python_api.models.app_of_the_day import AppOfTheDay
from flathub_python_api.models.apps_of_the_week import AppsOfTheWeek

class AppPicksRoutes(flatpak_apis.AppPicksApi):
        
    def get_app_of_the_day(self, date: Optional[datetime.date | str] = None) -> AppOfTheDay:
        """
        Get the app of the day for a specific date.
        
        Args:
            date (datetime.date | str, optional): The date for which to get the app of the day. Defaults to None.
        
        Returns:
            AppOfTheDay: The app of the day information.
        """
        if date is None:
            date = datetime.date.today()
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        return self.get_app_of_the_day_app_picks_app_of_the_day_date_get(var_date=date)

    def get_apps_of_the_week(self, date: Optional[datetime.date | str] = None) -> AppsOfTheWeek:
        """
        Get the apps of the week for a specific date.
        
        Args:
            date (datetime.date | str, optional): The date for which to get the app of the week. Defaults to None.
        
        Returns:
            AppsOfTheWeek: The apps of the week information.
        """
        if date is None:
            date = datetime.date.today()
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        return self.get_app_of_the_week_app_picks_apps_of_the_week_date_get(var_date=date)
