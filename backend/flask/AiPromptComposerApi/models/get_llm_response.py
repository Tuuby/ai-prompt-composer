from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from AiPromptComposerApi.models.base_model import Model
from AiPromptComposerApi import util


class GetLlmResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, models=None):  # noqa: E501
        """GetLlmResponse - a model defined in OpenAPI

        :param models: The models of this GetLlmResponse.  # noqa: E501
        :type models: List[str]
        """
        self.openapi_types = {
            'models': List[str]
        }

        self.attribute_map = {
            'models': 'models'
        }

        self._models = models

    @classmethod
    def from_dict(cls, dikt) -> 'GetLlmResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetLlmResponse of this GetLlmResponse.  # noqa: E501
        :rtype: GetLlmResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def models(self) -> List[str]:
        """Gets the models of this GetLlmResponse.

        Unique names of available LLMs  # noqa: E501

        :return: The models of this GetLlmResponse.
        :rtype: List[str]
        """
        return self._models

    @models.setter
    def models(self, models: List[str]):
        """Sets the models of this GetLlmResponse.

        Unique names of available LLMs  # noqa: E501

        :param models: The models of this GetLlmResponse.
        :type models: List[str]
        """

        self._models = models
