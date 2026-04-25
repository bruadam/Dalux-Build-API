'use strict';

/**
 * Configuration for the Dalux Build API client.
 */
class Configuration {
  /**
   * @param {object} options
   * @param {string} options.baseUrl  - The API base URL provided by Dalux (e.g. https://api.dalux.com/build)
   * @param {string} options.apiKey  - Your company-specific X-API-KEY
   */
  constructor({ baseUrl, apiKey } = {}) {
    if (!baseUrl) {
      throw new Error('baseUrl is required');
    }
    if (!apiKey) {
      throw new Error('apiKey is required');
    }
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.apiKey = apiKey;
  }
}

module.exports = Configuration;
