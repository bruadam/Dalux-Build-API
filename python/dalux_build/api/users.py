"""Users API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class UsersApi:
    """Methods for users."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def get_user(self, user_id: str) -> Any:
        """GET /1.1/users/{userId}."""
        return self._client.get(f"/1.1/users/{user_id}")

    def list_project_users(
        self, project_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /1.2/projects/{projectId}/users."""
        return self._client.get(
            f"/1.2/projects/{project_id}/users", params=params
        )

    def get_project_user(self, project_id: str, user_id: str) -> Any:
        """GET /1.1/projects/{projectId}/users/{userId}."""
        return self._client.get(
            f"/1.1/projects/{project_id}/users/{user_id}"
        )
