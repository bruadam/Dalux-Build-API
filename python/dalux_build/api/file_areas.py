"""File Areas API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class FileAreasApi:
    """Methods for file areas on a project."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def get_file_areas(
        self, project_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /5.1/projects/{projectId}/file_areas."""
        return self._client.get(
            f"/5.1/projects/{project_id}/file_areas", params=params
        )

    def get_file_area(self, project_id: str, file_area_id: str) -> Any:
        """GET /1.0/projects/{projectId}/file_areas/{fileAreaId}."""
        return self._client.get(
            f"/1.0/projects/{project_id}/file_areas/{file_area_id}"
        )
