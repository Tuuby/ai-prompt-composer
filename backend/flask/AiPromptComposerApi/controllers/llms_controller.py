import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from AiPromptComposerApi.models.error_information import ErrorInformation  # noqa: E501
from AiPromptComposerApi.models.get_llm_response import GetLlmResponse  # noqa: E501
from AiPromptComposerApi import util

import openai

def llms_get(authorization=None):  # noqa: E501
    """Gets the llm response, based on the supplied prompt data

    Builds a prompt from the prompt data and sends the LLM response back. # noqa: E501

    :param authorization: JWT token with authorization information.
    :type authorization: str

    :rtype: Union[GetLlmResponse, Tuple[GetLlmResponse, int], Tuple[GetLlmResponse, int, Dict[str, str]]
    """

    openai.api_key = "EMPTY"
    openai.api_base = "http://{hostname}/v1"

    models = openai.Model.list()
    modelIds = [item.id for item in models.data]

    return modelIds
