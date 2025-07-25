# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.vending_api import VendingApi


class TestVendingApi(unittest.TestCase):
    """VendingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VendingApi()

    def tearDown(self) -> None:
        pass

    def test_app_info_vendingapp_app_id_info_get(self) -> None:
        """Test case for app_info_vendingapp_app_id_info_get

        App Info
        """
        pass

    def test_cancel_tokens_vendingapp_app_id_tokens_cancel_post(self) -> None:
        """Test case for cancel_tokens_vendingapp_app_id_tokens_cancel_post

        Cancel Tokens
        """
        pass

    def test_create_tokens_vendingapp_app_id_tokens_post(self) -> None:
        """Test case for create_tokens_vendingapp_app_id_tokens_post

        Create Tokens
        """
        pass

    def test_get_app_vending_setup_vendingapp_app_id_setup_get(self) -> None:
        """Test case for get_app_vending_setup_vendingapp_app_id_setup_get

        Get App Vending Setup
        """
        pass

    def test_get_dashboard_link_vending_status_dashboardlink_get(self) -> None:
        """Test case for get_dashboard_link_vending_status_dashboardlink_get

        Get Dashboard Link
        """
        pass

    def test_get_global_vending_config_vending_config_get(self) -> None:
        """Test case for get_global_vending_config_vending_config_get

        Get Global Vending Config
        """
        pass

    def test_get_redeemable_tokens_vendingapp_app_id_tokens_get(self) -> None:
        """Test case for get_redeemable_tokens_vendingapp_app_id_tokens_get

        Get Redeemable Tokens
        """
        pass

    def test_post_app_vending_setup_vendingapp_app_id_setup_post(self) -> None:
        """Test case for post_app_vending_setup_vendingapp_app_id_setup_post

        Post App Vending Setup
        """
        pass

    def test_post_app_vending_status_vendingapp_app_id_post(self) -> None:
        """Test case for post_app_vending_status_vendingapp_app_id_post

        Post App Vending Status
        """
        pass

    def test_redeem_token_vendingapp_app_id_tokens_redeem_token_post(self) -> None:
        """Test case for redeem_token_vendingapp_app_id_tokens_redeem_token_post

        Redeem Token
        """
        pass

    def test_start_onboarding_vending_status_onboarding_post(self) -> None:
        """Test case for start_onboarding_vending_status_onboarding_post

        Start Onboarding
        """
        pass

    def test_status_vending_status_get(self) -> None:
        """Test case for status_vending_status_get

        Status
        """
        pass


if __name__ == '__main__':
    unittest.main()
