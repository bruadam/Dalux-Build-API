'use strict';

/**
 * API methods for users.
 */
class UsersApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Get a specific user.
   * GET /1.1/users/{userId}
   * @param {string} userId
   * @returns {Promise<object>}
   */
  getUser(userId) {
    return this._client.get(`/1.1/users/${userId}`);
  }

  /**
   * Get users on a project.
   * GET /1.2/projects/{projectId}/users
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listProjectUsers(projectId, params = {}) {
    return this._client.get(`/1.2/projects/${projectId}/users`, params);
  }

  /**
   * Get a specific user on a project.
   * GET /1.1/projects/{projectId}/users/{userId}
   * @param {string} projectId
   * @param {string} userId
   * @returns {Promise<object>}
   */
  getProjectUser(projectId, userId) {
    return this._client.get(`/1.1/projects/${projectId}/users/${userId}`);
  }
}

module.exports = UsersApi;
