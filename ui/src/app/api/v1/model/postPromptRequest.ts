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
 * The input data to prompt to the LLM.
 */
export interface PostPromptRequest { 
    /**
     * Name of the desired LLM.
     */
    modelName: string;
    /**
     * The input message from a user. Use \'{userPrompt}\'\' as placeholder in template.
     */
    userPrompt: string;
    /**
     * The specific instructions to the LLM on how to execute the tasks. Use \'{systemPrompt}\'\' as placeholder in template.
     */
    systemPrompt: string;
    /**
     * JSON of additional data containing the customers information. Use \'{inputData}\'\' as placeholder in template.
     */
    inputData: object;
    /**
     * The template to define how the prompt data gets assembled into one prompt string.
     */
    template: string;
}

