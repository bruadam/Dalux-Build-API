"""Project Templates API."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class ProjectTemplatesApi:
    """Methods for project templates."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def list_project_templates(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /1.1/projectTemplates — All templates on the company profile."""
        return self._client.get("/1.1/projectTemplates", params=params)
