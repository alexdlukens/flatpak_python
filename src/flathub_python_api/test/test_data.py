# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.data import Data

class TestData(unittest.TestCase):
    """Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Data:
        """Test Data
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Data`
        """
        model = Data()
        if include_optional:
            return Data(
                code = '',
                state = '',
                error = '',
                error_description = '',
                error_uri = ''
            )
        else:
            return Data(
                code = '',
                state = '',
                error = '',
        )
        """

    def testData(self):
        """Test Data"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
