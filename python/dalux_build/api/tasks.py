"""Tasks API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class TasksApi:
    """Methods for tasks, approvals, safety issues, observations and good practices."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def get_project_tasks(
        self, project_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /5.1/projects/{projectId}/tasks."""
        return self._client.get(f"/5.1/projects/{project_id}/tasks", params=params)

    def get_task(self, project_id: str, task_id: str) -> Any:
        """GET /3.3/projects/{projectId}/tasks/{taskId}."""
        return self._client.get(f"/3.3/projects/{project_id}/tasks/{task_id}")

    def get_project_task_changes(
        self, project_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /2.2/projects/{projectId}/tasks/changes."""
        return self._client.get(
            f"/2.2/projects/{project_id}/tasks/changes", params=params
        )

    def get_project_task_attachments(
        self, project_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /1.1/projects/{projectId}/tasks/attachments."""
        return self._client.get(
            f"/1.1/projects/{project_id}/tasks/attachments", params=params
        )
