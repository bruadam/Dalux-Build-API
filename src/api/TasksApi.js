'use strict';

/**
 * API methods for tasks, approvals, safety issues, observations and good practices.
 */
class TasksApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Retrieve tasks, approvals, safety issues, safety observations and good practices on a project.
  * GET /5.2/projects/{projectId}/tasks
   * @param {string} projectId
   * @param {object} [params] - Optional filters (e.g. updatedAfter, status, typeFilter)
   * @returns {Promise<object>}
   */
  getProjectTasks(projectId, params = {}) {
    return this._client.get(`/5.2/projects/${projectId}/tasks`, params);
  }

  /**
   * Retrieve all tasks on a project by following bookmark pagination automatically.
   * Combines all pages into a single array of items.
   * @param {string} projectId
   * @param {object} [params] - Optional filters (e.g. updatedAfter, status, typeFilter)
   * @returns {Promise<object[]>} All task items across all pages
   */
  async getAllProjectTasks(projectId, params = {}) {
    const allItems = [];
    let currentParams = { ...params };
    let hasNextPage = true;

    while (hasNextPage) {
      const response = await this._client.get(`/5.2/projects/${projectId}/tasks`, currentParams);
      if (Array.isArray(response.items)) {
        allItems.push(...response.items);
      }
      const nextLink = (response.links || []).find(l => l.rel === 'nextPage');
      if (nextLink) {
        const bookmark = new URL(nextLink.href).searchParams.get('bookmark');
        currentParams = { ...params, bookmark };
      } else {
        hasNextPage = false;
      }
    }
    return allItems;
  }

  /**
   * Retrieve a specific task/approval/safety issue/safety observation/good practice.
   * GET /3.3/projects/{projectId}/tasks/{taskId}
   * @param {string} projectId
   * @param {string} taskId
   * @returns {Promise<object>}
   */
  getTask(projectId, taskId) {
    return this._client.get(`/3.3/projects/${projectId}/tasks/${taskId}`);
  }

  /**
   * Retrieve task changes on a project in incremental updates.
   * GET /2.2/projects/{projectId}/tasks/changes
   * @param {string} projectId
   * @param {object} [params] - Optional filters (e.g. updatedAfter)
   * @returns {Promise<object>}
   */
  getProjectTaskChanges(projectId, params = {}) {
    return this._client.get(`/2.2/projects/${projectId}/tasks/changes`, params);
  }

  /**
   * Retrieve attachments on tasks on a project.
   * GET /1.1/projects/{projectId}/tasks/attachments
   * @param {string} projectId
   * @param {object} [params] - Optional filters (e.g. updatedAfter)
   * @returns {Promise<object>}
   */
  getProjectTaskAttachments(projectId, params = {}) {
    return this._client.get(`/1.1/projects/${projectId}/tasks/attachments`, params);
  }
}

module.exports = TasksApi;
