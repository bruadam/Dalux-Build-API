'use strict';

const axios = require('axios');

/**
 * Base HTTP client that attaches the X-API-KEY header to every request.
 */
class ApiClient {
  /**
   * @param {import('./configuration')} configuration
   */
  constructor(configuration) {
    if (!configuration) {
      throw new Error('configuration is required');
    }
    this.configuration = configuration;

    this._axios = axios.create({
      baseURL: configuration.baseUrl,
      headers: {
        'X-API-KEY': configuration.apiKey,
        'Content-Type': 'application/json',
      },
    });
  }

  /**
   * Perform a GET request.
   * @param {string} path  - URL path (e.g. '/5.1/projects')
   * @param {object} [params] - Query string parameters
   * @returns {Promise<any>} Parsed response body
   */
  async get(path, params = {}) {
    const response = await this._axios.get(path, { params });
    return response.data;
  }

  /**
   * Perform a POST request.
   * @param {string} path
   * @param {object} [body]
   * @param {object} [params]
   * @param {object} [config] - Extra axios config (e.g. custom headers or responseType)
   * @returns {Promise<any>}
   */
  async post(path, body = {}, params = {}, config = {}) {
    const response = await this._axios.post(path, body, { params, ...config });
    return response.data;
  }

  /**
   * Perform a PATCH request.
   * @param {string} path
   * @param {object} [body]
   * @param {object} [params]
   * @returns {Promise<any>}
   */
  async patch(path, body = {}, params = {}) {
    const response = await this._axios.patch(path, body, { params });
    return response.data;
  }

  /**
   * Perform a DELETE request.
   * @param {string} path
   * @param {object} [params]
   * @returns {Promise<any>}
   */
  async delete(path, params = {}) {
    const response = await this._axios.delete(path, { params });
    return response.data;
  }
}

module.exports = ApiClient;
