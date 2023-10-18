import unittest

from flask import json

from AiPromptComposerApi.models.error_information import ErrorInformation  # noqa: E501
from AiPromptComposerApi.models.get_llm_response import GetLlmResponse  # noqa: E501
from AiPromptComposerApi.test import BaseTestCase


class TestLLMsController(BaseTestCase):
    """LLMsController integration test stubs"""

    def test_llms_get(self):
        """Test case for llms_get

        Gets the llm response, based on the supplied prompt data
        """
        headers = { 
            'Accept': 'application/json',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
        }
        response = self.client.open(
            '/api/llms',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
