"""File Revisions API."""
from ..api_client import ApiClient


class FileRevisionsApi:
    """Methods for file revision content."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def get_file_revision_content(
        self,
        project_id: str,
        file_area_id: str,
        file_id: str,
        file_revision_id: str,
    ):
        """GET /2.0/.../files/{fileId}/revisions/{fileRevisionId}/content."""
        return self._client.get(
            f"/2.0/projects/{project_id}/file_areas/{file_area_id}"
            f"/files/{file_id}/revisions/{file_revision_id}/content"
        )
