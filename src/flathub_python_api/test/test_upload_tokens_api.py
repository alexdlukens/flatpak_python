# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.upload_tokens_api import UploadTokensApi


class TestUploadTokensApi(unittest.TestCase):
    """UploadTokensApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UploadTokensApi()

    def tearDown(self) -> None:
        pass

    def test_create_upload_token_upload_tokens_app_id_post(self) -> None:
        """Test case for create_upload_token_upload_tokens_app_id_post

        Create Upload Token
        """
        pass

    def test_get_upload_tokens_upload_tokens_app_id_get(self) -> None:
        """Test case for get_upload_tokens_upload_tokens_app_id_get

        Get Upload Tokens
        """
        pass

    def test_revoke_upload_token_upload_tokens_token_id_revoke_post(self) -> None:
        """Test case for revoke_upload_token_upload_tokens_token_id_revoke_post

        Revoke Upload Token
        """
        pass


if __name__ == '__main__':
    unittest.main()
