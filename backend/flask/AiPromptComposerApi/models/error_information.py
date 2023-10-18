from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from AiPromptComposerApi.models.base_model import Model
from AiPromptComposerApi import util


class ErrorInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, message=None):  # noqa: E501
        """ErrorInformation - a model defined in OpenAPI

        :param code: The code of this ErrorInformation.  # noqa: E501
        :type code: int
        :param message: The message of this ErrorInformation.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'code': int,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorInformation of this ErrorInformation.  # noqa: E501
        :rtype: ErrorInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this ErrorInformation.

        Some unique error code.  # noqa: E501

        :return: The code of this ErrorInformation.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this ErrorInformation.

        Some unique error code.  # noqa: E501

        :param code: The code of this ErrorInformation.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ErrorInformation.

        Error message.  # noqa: E501

        :return: The message of this ErrorInformation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ErrorInformation.

        Error message.  # noqa: E501

        :param message: The message of this ErrorInformation.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message