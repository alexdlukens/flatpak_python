from typing import Optional
from openapi_client import ApiClient, Configuration
import openapi_client.api as flatpak_apis
from flatpak_python.schemas.general import HealthCheckResponse


class FlatpakPythonClient:
    """
    A client for interacting with the Flatpak Python API.

    This client is used to make requests to the Flatpak Python API endpoints.
    It inherits from ApiClient and can be customized as needed.
    """

    def __init__(self, config: Optional[Configuration] = None) -> None:
        self.client = ApiClient(configuration=config)

    def init_apis(self) -> None:
        self.healthcheck_api = flatpak_apis.HealthcheckApi(self.client)

    def ping(self) -> HealthCheckResponse:
        """
        Check the health of the Flatpak Python API.

        Returns:
            HealthCheckResponse: The health check response.
        """
        return HealthCheckResponse.model_validate(
            self.healthcheck_api.healthcheck_status_get()
        )
