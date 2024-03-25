import connexion
import openai
import sys
import os

from typing import Dict
from typing import Tuple
from typing import Union

from AiPromptComposerApi.models.error_information import ErrorInformation  # noqa: E501
from AiPromptComposerApi.models.post_prompt_request import PostPromptRequest  # noqa: E501
from AiPromptComposerApi.models.post_prompt_response import PostPromptResponse  # noqa: E501
from AiPromptComposerApi import util


def prompt_post(authorization=None, post_prompt_request=None):  # noqa: E501
    """Prompts a message to a LLM and gets response, based on the supplied prompt data

    Builds a prompt from the prompt data and sends the LLM response back. # noqa: E501

    :param authorization: JWT token with authorization information.
    :type authorization: str
    :param post_prompt_request: 
    :type post_prompt_request: dict | bytes
^
    :rtype: Union[PostPromptResponse, Tuple[PostPromptResponse, int], Tuple[PostPromptResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_prompt_request = PostPromptRequest.from_dict(connexion.request.get_json())  # noqa: E501

    openAiApiBase = os.getenv('OPEN_AI_API_BASE')
    openAiApiKey = os.getenv('OPEN_AI_API_KEY')
    
    if openAiApiBase == "OPEN_AI_API_BASE":
        print('Environment variable OPEN_AI_API_BASE has no value!', file=sys.stderr)

    if openAiApiKey == "OPEN_AI_API_KEY":
        print('Environment variable OPEN_AI_API_KEY has no value. This is OK for fastchat or other api compatible applications.')
    
    openai.api_key = openAiApiKey
    openai.base_url = openAiApiBase

    prompt = post_prompt_request.template.replace('{userPrompt}', post_prompt_request.user_prompt).replace('{systemPrompt}', post_prompt_request.system_prompt).replace('{inputData}', str(post_prompt_request.input_data))

    completion = openai.chat.completions.create(model=post_prompt_request.model_name, messages=prompt, max_tokens=512,
                                                 temperature=0)
    response = completion.choices[0].message.content
    return PostPromptResponse(response)
