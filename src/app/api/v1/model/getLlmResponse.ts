/**
 * AI Prompt Composer API
 * This API is for quickly adjusting prompt data to improve LLM Output
 *
 * The version of the OpenAPI document: 0.2
 * Contact: trompell@th-brandenburg.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * Information about the available LLMs.
 */
export interface GetLlmResponse { 
    /**
     * Unique names of available LLMs
     */
    models?: Array<string>;
}

