'use strict';

/**
 * API methods for folders within a file area.
 */
class FoldersApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Browse all folders on the given project and file area.
   * GET /5.1/projects/{projectId}/file_areas/{fileAreaId}/folders
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listFolders(projectId, fileAreaId, params = {}) {
    return this._client.get(
      `/5.1/projects/${projectId}/file_areas/${fileAreaId}/folders`,
      params,
    );
  }

  /**
   * Retrieve a specific folder.
   * GET /5.0/projects/{projectId}/file_areas/{fileAreaId}/folders/{folderId}
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {string} folderId
   * @returns {Promise<object>}
   */
  getFolder(projectId, fileAreaId, folderId) {
    return this._client.get(
      `/5.0/projects/${projectId}/file_areas/${fileAreaId}/folders/${folderId}`,
    );
  }

  /**
   * Retrieve all properties for each file type in a specific folder.
   * GET /1.0/projects/{projectId}/file_areas/{fileAreaId}/folders/{folderId}/files/properties/1.0/mappings
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {string} folderId
   * @returns {Promise<object>}
   */
  getFolderFilesProperties(projectId, fileAreaId, folderId) {
    return this._client.get(
      `/1.0/projects/${projectId}/file_areas/${fileAreaId}/folders/${folderId}/files/properties/1.0/mappings`,
    );
  }
}

module.exports = FoldersApi;
