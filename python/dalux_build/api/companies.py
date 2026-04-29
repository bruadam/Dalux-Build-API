"""Companies API (project companies)."""
from typing import Any, Dict, Optional

from ..api_client import ApiClient


class CompaniesApi:
    """Methods for managing companies on a project."""

    def __init__(self, api_client: ApiClient) -> None:
        self._client = api_client

    def list_project_companies(
        self, project_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """GET /3.1/projects/{projectId}/companies."""
        return self._client.get(f"/3.1/projects/{project_id}/companies", params=params)

    def get_project_company(self, project_id: str, company_id: str) -> Any:
        """GET /3.0/projects/{projectId}/companies/{companyId}."""
        return self._client.get(
            f"/3.0/projects/{project_id}/companies/{company_id}"
        )

    def create_project_company(
        self, project_id: str, body: Dict[str, Any]
    ) -> Any:
        """POST /3.1/projects/{projectId}/companies."""
        return self._client.post(
            f"/3.1/projects/{project_id}/companies", json=body
        )

    def update_project_company(
        self, project_id: str, company_id: str, body: Dict[str, Any]
    ) -> Any:
        """PATCH /3.0/projects/{projectId}/companies/{companyId}."""
        return self._client.patch(
            f"/3.0/projects/{project_id}/companies/{company_id}", json=body
        )
