# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.review_response import ReviewResponse

class TestReviewResponse(unittest.TestCase):
    """ReviewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewResponse:
        """Test ReviewResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewResponse`
        """
        model = ReviewResponse()
        if include_optional:
            return ReviewResponse(
                github_issue_url = ''
            )
        else:
            return ReviewResponse(
                github_issue_url = '',
        )
        """

    def testReviewResponse(self):
        """Test ReviewResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
