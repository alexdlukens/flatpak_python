# coding: utf-8

"""
    Flathub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.flathub_users_result import FlathubUsersResult

class TestFlathubUsersResult(unittest.TestCase):
    """FlathubUsersResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlathubUsersResult:
        """Test FlathubUsersResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlathubUsersResult`
        """
        model = FlathubUsersResult()
        if include_optional:
            return FlathubUsersResult(
                users = [
                    openapi_client.models.user_result.UserResult(
                        id = 56, 
                        display_name = '', 
                        default_account = null, 
                        connected_accounts = [
                            null
                            ], 
                        accepted_publisher_agreement_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        roles = [
                            openapi_client.models.user_role_result.UserRoleResult(
                                name = '', 
                                has_role = True, )
                            ], 
                        github_repos = [
                            openapi_client.models.github_repository_result.GithubRepositoryResult(
                                id = 56, 
                                reponame = '', )
                            ], 
                        owned_apps = [
                            openapi_client.models.user_owned_app_result.UserOwnedAppResult(
                                app_id = '', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ],
                pagination = openapi_client.models.pagination.Pagination(
                    page = 56, 
                    page_size = 56, 
                    total = 56, 
                    total_pages = 56, )
            )
        else:
            return FlathubUsersResult(
                users = [
                    openapi_client.models.user_result.UserResult(
                        id = 56, 
                        display_name = '', 
                        default_account = null, 
                        connected_accounts = [
                            null
                            ], 
                        accepted_publisher_agreement_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        roles = [
                            openapi_client.models.user_role_result.UserRoleResult(
                                name = '', 
                                has_role = True, )
                            ], 
                        github_repos = [
                            openapi_client.models.github_repository_result.GithubRepositoryResult(
                                id = 56, 
                                reponame = '', )
                            ], 
                        owned_apps = [
                            openapi_client.models.user_owned_app_result.UserOwnedAppResult(
                                app_id = '', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ],
                pagination = openapi_client.models.pagination.Pagination(
                    page = 56, 
                    page_size = 56, 
                    total = 56, 
                    total_pages = 56, ),
        )
        """

    def testFlathubUsersResult(self):
        """Test FlathubUsersResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
