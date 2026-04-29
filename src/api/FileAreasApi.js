'use strict';

/**
 * API methods for file areas on a project.
 */
class FileAreasApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Retrieve the file areas on the given project.
   * GET /5.1/projects/{projectId}/file_areas
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  getFileAreas(projectId, params = {}) {
    return this._client.get(`/5.1/projects/${projectId}/file_areas`, params);
  }

  /**
   * Retrieve a specific file area.
   * GET /1.0/projects/{projectId}/file_areas/{fileAreaId}
   * @param {string} projectId
   * @param {string} fileAreaId
   * @returns {Promise<object>}
   */
  getFileArea(projectId, fileAreaId) {
    return this._client.get(`/1.0/projects/${projectId}/file_areas/${fileAreaId}`);
  }
}

module.exports = FileAreasApi;
