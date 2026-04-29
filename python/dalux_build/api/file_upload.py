"""File Upload API (chunked upload)."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class FileUploadApi:
    """Methods for chunked file uploads."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def create_upload(
        self, project_id: str, file_area_id: str, body: Dict[str, Any]
    ) -> Any:
        """POST /1.0/.../upload — Create an upload slot and return its GUID."""
        return self._client.post(
            f"/1.0/projects/{project_id}/file_areas/{file_area_id}/upload",
            json=body,
        )

    def upload_file_part(
        self,
        project_id: str,
        file_area_id: str,
        upload_guid: str,
        chunk: bytes,
    ) -> Any:
        """POST /1.0/.../upload/{uploadGuid} — Upload a binary file chunk."""
        return self._client.post(
            f"/1.0/projects/{project_id}/file_areas/{file_area_id}/upload/{upload_guid}",
            data=chunk,
            headers={"Content-Type": "application/octet-stream"},
        )

    def finish_upload(
        self,
        project_id: str,
        file_area_id: str,
        upload_guid: str,
        body: Dict[str, Any],
    ) -> Any:
        """POST /2.0/.../upload/{uploadGuid}/finalize — Finalize the upload."""
        return self._client.post(
            f"/2.0/projects/{project_id}/file_areas/{file_area_id}"
            f"/upload/{upload_guid}/finalize",
            json=body,
        )
