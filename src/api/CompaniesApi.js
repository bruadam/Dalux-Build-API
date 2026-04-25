'use strict';

/**
 * API methods for managing companies on a project.
 */
class CompaniesApi {
  /**
   * @param {import('../apiClient')} apiClient
   */
  constructor(apiClient) {
    this._client = apiClient;
  }

  /**
   * Get companies on a project.
   * GET /3.1/projects/{projectId}/companies
   * @param {string} projectId
   * @param {object} [params]
   * @returns {Promise<object>}
   */
  listProjectCompanies(projectId, params = {}) {
    return this._client.get(`/3.1/projects/${projectId}/companies`, params);
  }

  /**
   * Get a specific company on a project.
   * GET /3.0/projects/{projectId}/companies/{companyId}
   * @param {string} projectId
   * @param {string} companyId
   * @returns {Promise<object>}
   */
  getProjectCompany(projectId, companyId) {
    return this._client.get(`/3.0/projects/${projectId}/companies/${companyId}`);
  }

  /**
   * Add a company to a project.
   * POST /3.1/projects/{projectId}/companies
   * @param {string} projectId
   * @param {object} body
   * @returns {Promise<object>}
   */
  createProjectCompany(projectId, body) {
    return this._client.post(`/3.1/projects/${projectId}/companies`, body);
  }

  /**
   * Update a company on a project.
   * PATCH /3.0/projects/{projectId}/companies/{companyId}
   * @param {string} projectId
   * @param {string} companyId
   * @param {object} body
   * @returns {Promise<object>}
   */
  updateProjectCompany(projectId, companyId, body) {
    return this._client.patch(`/3.0/projects/${projectId}/companies/${companyId}`, body);
  }
}

module.exports = CompaniesApi;
