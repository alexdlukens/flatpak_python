import datetime
from typing import Optional

import openapi_client.api as flatpak_apis
from openapi_client.models.app_of_the_day import AppOfTheDay

class AppPicksRoutes(flatpak_apis.AppPicksApi):
        
    def get_app_of_the_day(self, date: Optional[datetime.date | str] = None) -> AppOfTheDay:
        """
        Get the app of the day for a specific date.
        
        Args:
            date (datetime.date | str, optional): The date for which to get the app of the day. Defaults to None.
        
        Returns:
            dict: The app of the day information.
        """
        if date is None:
            date = datetime.date.today()
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        return self.get_app_of_the_day_app_picks_app_of_the_day_date_get(var_date=date)
