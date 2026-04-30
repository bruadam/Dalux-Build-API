"""Folders API."""
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from urllib.parse import parse_qs, urlparse

from ..api_client import ApiClient

if TYPE_CHECKING:
    from .files import FilesApi


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

    def get_all_folders(
        self,
        project_id: str,
        file_area_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> List[Any]:
        """Retrieve all folders by following bookmark pagination automatically.

        Combines all pages into a single list of items.
        """
        all_items: List[Any] = []
        current_params: Dict[str, Any] = dict(params or {})
        has_next_page = True

        while has_next_page:
            response = self._client.get(
                f"/5.1/projects/{project_id}/file_areas/{file_area_id}/folders",
                params=current_params,
            )
            items = response.get("items") if response else None
            if items:
                all_items.extend(items)
            next_link = next(
                (l for l in (response.get("links") or []) if l.get("rel") == "nextPage"),
                None,
            )
            if next_link:
                qs = parse_qs(urlparse(next_link["href"]).query)
                bookmark = qs.get("bookmark", [None])[0]
                current_params = {**dict(params or {}), "bookmark": bookmark}
            else:
                has_next_page = False

        return all_items

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

    def get_file_area_tree(
        self,
        project_id: str,
        file_area_id: str,
        files_api: Optional["FilesApi"] = None,
        verbose: bool = False,
    ) -> Dict[str, Any]:
        """Build the complete folder+file tree for a file area efficiently.

        Fetches all folders (and optionally all files) and assembles them into a
        nested tree. When *files_api* is provided, folders and files are fetched
        **concurrently** in two threads.

        Each node has the shape::

            {
                "id": "<folderId | None for root>",
                "name": "<folder name>",
                "path": "parent/child/name",
                "raw":  <original API item>,
                "children": [<child folder nodes>, ...],
                "files": [<file items belonging to this folder>, ...],
            }

        The returned root node represents the file-area root (``id=None``).

        Args:
            project_id: Project ID.
            file_area_id: File area ID.
            files_api: Optional :class:`FilesApi` instance. When provided, files
                are fetched in parallel and attached to their folder nodes.
            verbose: If ``True``, print progress information.

        Returns:
            Root tree node (dict).
        """

        def _fetch_files():
            return files_api.get_all_files(project_id, file_area_id, verbose=verbose)

        if files_api is not None:
            with ThreadPoolExecutor(max_workers=2) as executor:
                folders_fut = executor.submit(self.get_all_folders, project_id, file_area_id)
                files_fut = executor.submit(_fetch_files)
                all_folders = folders_fut.result()
                all_files = files_fut.result()
        else:
            all_folders = self.get_all_folders(project_id, file_area_id)
            all_files = []

        if verbose:
            print(f"Building tree: {len(all_folders)} folder(s), {len(all_files)} file(s)")

        # --- helpers to extract fields from varying API shapes ---
        def _fid(item: Any) -> Optional[str]:
            d = item.get("data") or {}
            return d.get("id") or d.get("folderId") or item.get("id") or item.get("folderId")

        def _pid(item: Any) -> Optional[str]:
            d = item.get("data") or {}
            return d.get("parentFolderId") or d.get("parentId") or item.get("parentFolderId") or item.get("parentId")

        def _name(item: Any) -> str:
            d = item.get("data") or {}
            return d.get("name") or d.get("folderName") or item.get("name") or _fid(item) or "?"

        # --- build node map ---
        nodes: Dict[str, Dict[str, Any]] = {}
        for folder in all_folders:
            fid = _fid(folder)
            if fid is None:
                continue
            nodes[fid] = {
                "id": fid,
                "name": _name(folder),
                "path": "",
                "raw": folder,
                "children": [],
                "files": [],
            }

        # --- wire parent → child relationships ---
        root: Dict[str, Any] = {
            "id": None,
            "name": file_area_id,
            "path": "",
            "raw": None,
            "children": [],
            "files": [],
        }
        for folder in all_folders:
            fid = _fid(folder)
            if fid is None:
                continue
            pid = _pid(folder)
            parent = nodes.get(pid, root)
            parent["children"].append(nodes[fid])

        # --- compute slash-separated paths ---
        def _set_paths(node: Dict[str, Any], parent_path: str) -> None:
            node["path"] = f"{parent_path}/{node['name']}" if parent_path else node["name"]
            for child in node["children"]:
                _set_paths(child, node["path"])

        for child in root["children"]:
            _set_paths(child, "")

        # --- attach files to their folder nodes ---
        for f in all_files:
            fid = (f.get("data") or {}).get("folderId")
            target = nodes.get(fid, root)
            target["files"].append(f)

        return root
