# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.moderation_apps_response import ModerationAppsResponse

class TestModerationAppsResponse(unittest.TestCase):
    """ModerationAppsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModerationAppsResponse:
        """Test ModerationAppsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModerationAppsResponse`
        """
        model = ModerationAppsResponse()
        if include_optional:
            return ModerationAppsResponse(
                apps = [
                    openapi_client.models.moderation_app_item.ModerationAppItem(
                        appid = '', 
                        is_new_submission = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        request_types = [
                            'appdata'
                            ], )
                    ],
                apps_count = 56
            )
        else:
            return ModerationAppsResponse(
                apps = [
                    openapi_client.models.moderation_app_item.ModerationAppItem(
                        appid = '', 
                        is_new_submission = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        request_types = [
                            'appdata'
                            ], )
                    ],
                apps_count = 56,
        )
        """

    def testModerationAppsResponse(self):
        """Test ModerationAppsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
