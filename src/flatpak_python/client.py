from typing import Optional
from flathub_python_api import ApiClient, Configuration
import flathub_python_api.api as flatpak_apis
from flatpak_python.schemas.general import HealthCheckResponse
from flatpak_python.routes.app_picks import AppPicksRoutes

class FlatpakPythonClient:
    """
    A client for interacting with the FlatHub API.

    This client is used to make requests to the FlatHub API endpoints.
    It inherits from ApiClient and can be customized as needed.
    
    Will add flatpak daemon support in the future.
    """

    def __init__(self, config: Optional[Configuration] = None) -> None:
        self.client = ApiClient(configuration=config)

    def init_apis(self) -> None:
        self.healthcheck_api = flatpak_apis.HealthcheckApi(self.client)
        self.app_picks_api = AppPicksRoutes(self.client)

    def ping(self) -> HealthCheckResponse:
        """
        Check the health of the FlatHub API.

        Returns:
            HealthCheckResponse: The health check response.
        """
        return HealthCheckResponse.model_validate(
            self.healthcheck_api.healthcheck_status_get()
        )
