import unittest

from flask import json

from AiPromptComposerApi.models.error_information import ErrorInformation  # noqa: E501
from AiPromptComposerApi.models.post_prompt_request import PostPromptRequest  # noqa: E501
from AiPromptComposerApi.models.post_prompt_response import PostPromptResponse  # noqa: E501
from AiPromptComposerApi.test import BaseTestCase


class TestPromptController(BaseTestCase):
    """PromptController integration test stubs"""

    def test_prompt_post(self):
        """Test case for prompt_post

        Prompts a message to a LLM and gets response, based on the supplied prompt data
        """
        post_prompt_request = {"template":"template","systemPrompt":"systemPrompt","inputData":"{}","userPrompt":"userPrompt"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
        }
        response = self.client.open(
            '/api/prompt',
            method='POST',
            headers=headers,
            data=json.dumps(post_prompt_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
