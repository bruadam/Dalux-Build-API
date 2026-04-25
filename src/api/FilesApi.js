'use strict';

/**
 * API methods for files within a file area.
 */
class FilesApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Browse all files on the given project and file area.
   * GET /6.0/projects/{projectId}/file_areas/{fileAreaId}/files
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {object} [params] - Optional filters (e.g. folderId, updatedAfter)
   * @returns {Promise<object>}
   */
  listFiles(projectId, fileAreaId, params = {}) {
    return this._client.get(
      `/6.0/projects/${projectId}/file_areas/${fileAreaId}/files`,
      params,
    );
  }

  /**
   * Retrieve a specific file.
   * GET /5.0/projects/{projectId}/file_areas/{fileAreaId}/files/{fileId}
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {string} fileId
   * @returns {Promise<object>}
   */
  getFile(projectId, fileAreaId, fileId) {
    return this._client.get(
      `/5.0/projects/${projectId}/file_areas/${fileAreaId}/files/${fileId}`,
    );
  }

  /**
   * Retrieve properties mapping for a specific file.
   * GET /1.0/projects/{projectId}/file_areas/{fileAreaId}/files/{fileId}/properties/1.0/mappings
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {string} fileId
   * @returns {Promise<object>}
   */
  getFilePropertiesMapping(projectId, fileAreaId, fileId) {
    return this._client.get(
      `/1.0/projects/${projectId}/file_areas/${fileAreaId}/files/${fileId}/properties/1.0/mappings`,
    );
  }

  /**
   * Retrieve valid property values for a specific file property mapping.
   * GET /1.0/projects/{projectId}/file_areas/{fileAreaId}/files/properties/1.0/mappings/{filePropertyId}/values
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {string} filePropertyId
   * @returns {Promise<object>}
   */
  getFilePropertyMappingValues(projectId, fileAreaId, filePropertyId) {
    return this._client.get(
      `/1.0/projects/${projectId}/file_areas/${fileAreaId}/files/properties/1.0/mappings/${filePropertyId}/values`,
    );
  }
}

module.exports = FilesApi;
