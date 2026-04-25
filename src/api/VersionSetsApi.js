'use strict';

/**
 * API methods for version sets.
 */
class VersionSetsApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Retrieve the version sets on the given project.
   * GET /2.1/projects/{projectId}/version_sets
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  getVersionSets(projectId, params = {}) {
    return this._client.get(`/2.1/projects/${projectId}/version_sets`, params);
  }

  /**
   * Retrieve a specific version set.
   * GET /2.0/projects/{projectId}/version_sets/{versionSetId}
   * @param {string} projectId
   * @param {string} versionSetId
   * @returns {Promise<object>}
   */
  getVersionSet(projectId, versionSetId) {
    return this._client.get(`/2.0/projects/${projectId}/version_sets/${versionSetId}`);
  }

  /**
   * Browse all version sets on the given file area and project.
   * GET /2.1/projects/{projectId}/file_areas/{fileAreaId}/version_sets
   * @param {string} projectId
   * @param {string} fileAreaId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listFileAreaVersionSets(projectId, fileAreaId, params = {}) {
    return this._client.get(
      `/2.1/projects/${projectId}/file_areas/${fileAreaId}/version_sets`,
      params,
    );
  }

  /**
   * Browse all files on the given project and given version set.
   * GET /3.0/projects/{projectId}/version_sets/{versionSetId}/files
   * @param {string} projectId
   * @param {string} versionSetId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listVersionSetFiles(projectId, versionSetId, params = {}) {
    return this._client.get(
      `/3.0/projects/${projectId}/version_sets/${versionSetId}/files`,
      params,
    );
  }
}

module.exports = VersionSetsApi;
