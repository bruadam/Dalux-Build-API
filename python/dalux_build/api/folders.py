"""Folders API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class FoldersApi:
    """Methods for folders within a file area."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def list_folders(
        self,
        project_id: str,
        file_area_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """GET /5.1/projects/{projectId}/file_areas/{fileAreaId}/folders."""
        return self._client.get(
            f"/5.1/projects/{project_id}/file_areas/{file_area_id}/folders",
            params=params,
        )

    def get_folder(
        self, project_id: str, file_area_id: str, folder_id: str
    ) -> Any:
        """GET /5.0/.../folders/{folderId}."""
        return self._client.get(
            f"/5.0/projects/{project_id}/file_areas/{file_area_id}/folders/{folder_id}"
        )

    def get_folder_files_properties(
        self, project_id: str, file_area_id: str, folder_id: str
    ) -> Any:
        """GET /1.0/.../folders/{folderId}/files/properties/1.0/mappings."""
        return self._client.get(
            f"/1.0/projects/{project_id}/file_areas/{file_area_id}"
            f"/folders/{folder_id}/files/properties/1.0/mappings"
        )
