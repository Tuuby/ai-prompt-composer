import os
import sys
import openai

from AiPromptComposerApi.models.error_information import ErrorInformation  # noqa: E501
from AiPromptComposerApi.models.get_llm_response import GetLlmResponse  # noqa: E501

def llms_get(authorization=None):  # noqa: E501
    """Gets the llm response, based on the supplied prompt data

    Builds a prompt from the prompt data and sends the LLM response back. # noqa: E501

    :param authorization: JWT token with authorization information.
    :type authorization: str

    :rtype: Union[GetLlmResponse, Tuple[GetLlmResponse, int], Tuple[GetLlmResponse, int, Dict[str, str]]
    """

    openAiApiBase = os.getenv('OPEN_AI_API_BASE')
    openAiApiKey = os.getenv('OPEN_AI_API_KEY')
    
    if openAiApiBase == "OPEN_AI_API_BASE":
        print('Environment variable OPEN_AI_API_BASE has no value!', file=sys.stderr)

    if openAiApiKey == "OPEN_AI_API_KEY":
        print('Environment variable OPEN_AI_API_KEY has no value. This is OK for fastchat or other api compatible applications.')
    
    openai.api_key = openAiApiKey
    openai.api_base = openAiApiBase

    models = openai.Model.list()
    modelIds = [item.id for item in models.data]

    return GetLlmResponse(modelIds)
