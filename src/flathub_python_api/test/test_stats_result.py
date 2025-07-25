# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.stats_result import StatsResult

class TestStatsResult(unittest.TestCase):
    """StatsResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatsResult:
        """Test StatsResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatsResult`
        """
        model = StatsResult()
        if include_optional:
            return StatsResult(
                totals = {
                    'key' : 56
                    },
                countries = {
                    'key' : 56
                    },
                downloads_per_day = {
                    'key' : 56
                    },
                updates_per_day = {
                    'key' : 56
                    },
                delta_downloads_per_day = {
                    'key' : 56
                    },
                category_totals = [
                    openapi_client.models.stats_result_category_totals.StatsResultCategoryTotals(
                        category = '', 
                        count = 56, )
                    ]
            )
        else:
            return StatsResult(
                totals = {
                    'key' : 56
                    },
                countries = {
                    'key' : 56
                    },
                downloads_per_day = {
                    'key' : 56
                    },
                updates_per_day = {
                    'key' : 56
                    },
                delta_downloads_per_day = {
                    'key' : 56
                    },
                category_totals = [
                    openapi_client.models.stats_result_category_totals.StatsResultCategoryTotals(
                        category = '', 
                        count = 56, )
                    ],
        )
        """

    def testStatsResult(self):
        """Test StatsResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
