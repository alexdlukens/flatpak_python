# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tokens_response import TokensResponse

class TestTokensResponse(unittest.TestCase):
    """TokensResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokensResponse:
        """Test TokensResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokensResponse`
        """
        model = TokensResponse()
        if include_optional:
            return TokensResponse(
                tokens = [
                    openapi_client.models.token_response.TokenResponse(
                        id = 56, 
                        comment = '', 
                        app_id = '', 
                        scopes = [
                            ''
                            ], 
                        repos = [
                            ''
                            ], 
                        issued_at = 56, 
                        issued_to = '', 
                        expires_at = 56, 
                        revoked = True, )
                    ],
                is_direct_upload_app = True
            )
        else:
            return TokensResponse(
                tokens = [
                    openapi_client.models.token_response.TokenResponse(
                        id = 56, 
                        comment = '', 
                        app_id = '', 
                        scopes = [
                            ''
                            ], 
                        repos = [
                            ''
                            ], 
                        issued_at = 56, 
                        issued_to = '', 
                        expires_at = 56, 
                        revoked = True, )
                    ],
                is_direct_upload_app = True,
        )
        """

    def testTokensResponse(self):
        """Test TokensResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
