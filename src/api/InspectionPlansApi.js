'use strict';

/**
 * API methods for inspection plans.
 */
class InspectionPlansApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Browse all inspection plans on the given project.
   * GET /1.2/projects/{projectId}/inspectionPlans
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listInspectionPlans(projectId, params = {}) {
    return this._client.get(`/1.2/projects/${projectId}/inspectionPlans`, params);
  }

  /**
   * Browse all inspection plan items on the given project.
   * GET /1.1/projects/{projectId}/inspectionPlanItems
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listInspectionPlanItems(projectId, params = {}) {
    return this._client.get(`/1.1/projects/${projectId}/inspectionPlanItems`, params);
  }

  /**
   * Browse all inspection plan item zones on the given project.
   * GET /1.1/projects/{projectId}/inspectionPlanItemZones
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listInspectionPlanItemZones(projectId, params = {}) {
    return this._client.get(`/1.1/projects/${projectId}/inspectionPlanItemZones`, params);
  }

  /**
   * Browse all inspection plan registrations on the given project.
   * GET /2.1/projects/{projectId}/inspectionPlanRegistrations
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listInspectionPlanRegistrations(projectId, params = {}) {
    return this._client.get(
      `/2.1/projects/${projectId}/inspectionPlanRegistrations`,
      params,
    );
  }
}

module.exports = InspectionPlansApi;
