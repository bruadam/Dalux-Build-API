"""Files API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class FilesApi:
    """Methods for files within a file area."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def list_files(
        self,
        project_id: str,
        file_area_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """GET /6.0/projects/{projectId}/file_areas/{fileAreaId}/files."""
        return self._client.get(
            f"/6.0/projects/{project_id}/file_areas/{file_area_id}/files",
            params=params,
        )

    def get_file(
        self, project_id: str, file_area_id: str, file_id: str
    ) -> Any:
        """GET /5.0/projects/{projectId}/file_areas/{fileAreaId}/files/{fileId}."""
        return self._client.get(
            f"/5.0/projects/{project_id}/file_areas/{file_area_id}/files/{file_id}"
        )

    def get_file_properties_mapping(
        self, project_id: str, file_area_id: str, file_id: str
    ) -> Any:
        """GET .../files/{fileId}/properties/1.0/mappings."""
        return self._client.get(
            f"/1.0/projects/{project_id}/file_areas/{file_area_id}"
            f"/files/{file_id}/properties/1.0/mappings"
        )

    def get_file_property_mapping_values(
        self, project_id: str, file_area_id: str, file_property_id: str
    ) -> Any:
        """GET .../files/properties/1.0/mappings/{filePropertyId}/values."""
        return self._client.get(
            f"/1.0/projects/{project_id}/file_areas/{file_area_id}"
            f"/files/properties/1.0/mappings/{file_property_id}/values"
        )
