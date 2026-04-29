'use strict';

/**
 * API methods for work packages on a project.
 */
class WorkPackagesApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Browse all work packages on the given project.
   * GET /1.0/projects/{projectId}/workpackages
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listWorkPackages(projectId, params = {}) {
    return this._client.get(`/1.0/projects/${projectId}/workpackages`, params);
  }
}

module.exports = WorkPackagesApi;
