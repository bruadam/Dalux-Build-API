"""Projects API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class ProjectsApi:
    """Methods for managing projects.

    Args:
        api_client: Configured :class:`~dalux_build.api_client.ApiClient`.
    """

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def list_projects(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """GET /5.1/projects — List all available projects."""
        return self._client.get("/5.1/projects", params=params)

    def get_project(self, project_id: str) -> Any:
        """GET /5.0/projects/{projectId} — Get a specific project."""
        return self._client.get(f"/5.0/projects/{project_id}")

    def create_project(self, body: Dict[str, Any]) -> Any:
        """POST /5.0/projects — Create a new project."""
        return self._client.post("/5.0/projects", json=body)

    def update_project(self, project_id: str, body: Dict[str, Any]) -> Any:
        """PATCH /5.0/projects/{projectId} — Update a project."""
        return self._client.patch(f"/5.0/projects/{project_id}", json=body)

    def list_metadata_mappings_for_projects(self) -> Any:
        """GET /1.0/projects/metadata/1.0/mappings — Metadata for POST operations."""
        return self._client.get("/1.0/projects/metadata/1.0/mappings")

    def list_metadata_values_for_projects(self, key: str) -> Any:
        """GET /1.0/projects/metadata/1.0/mappings/{key}/values."""
        return self._client.get(f"/1.0/projects/metadata/1.0/mappings/{key}/values")

    def list_project_metadata(self, project_id: str) -> Any:
        """GET /1.0/projects/{projectId}/metadata."""
        return self._client.get(f"/1.0/projects/{project_id}/metadata")

    def list_project_metadata_mappings(self, project_id: str) -> Any:
        """GET /1.0/projects/{projectId}/metadata/1.0/mappings."""
        return self._client.get(
            f"/1.0/projects/{project_id}/metadata/1.0/mappings"
        )

    def list_project_metadata_values(self, project_id: str, key: str) -> Any:
        """GET /1.0/projects/{projectId}/metadata/1.0/mappings/{key}/values."""
        return self._client.get(
            f"/1.0/projects/{project_id}/metadata/1.0/mappings/{key}/values"
        )
