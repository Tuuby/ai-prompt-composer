import connexion
import openai

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

    openai.api_key = "EMPTY"
    openai.api_base =  "http://{hostname}/v1"


    modelname = "gpt-3.5-turbo"
    
    prompt = post_prompt_request.template.replace('{userPrompt}', post_prompt_request.user_prompt).replace('{systemPrompt}', post_prompt_request.system_prompt).replace('{inputData}', str(post_prompt_request.input_data))

    completion = openai.ChatCompletion.create(model=modelname, messages=prompt, max_tokens=512,
                                                 temperature=0)
    
    return completion.choices[0]['message']['content']
