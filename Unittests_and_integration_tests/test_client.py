#!/usr/bin/env python3
""" Test file for client.py
"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import PropertyMock, patch
from Unittests_and_integration_tests.fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    """ Test client.py
    """

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """ Mock the payload of a request
        """
        client = GithubOrgClient(org_name)

        # Call the method
        client.org

        mock_get.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Mock the payload of a request and check
            the name in the repo is the same in the payload
        """
        mock_repos_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_repos_payload
        mock_public_repos_url = 'http://mocked.url/repos'

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = mock_public_repos_url

            github_org_client = GithubOrgClient("some_org")

            # Get org repos
            public_repos = github_org_client.public_repos()

            # Check that the repo matches the payload
            self.assertEqual(public_repos,
                             [repo['name'] for repo in mock_repos_payload])

            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, 'my_license', True),
        ({"license": {"key": "other_license"}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test that githuborgclient returns the correct license
        """
        # Instantiate Org Client
        github_org_client = GithubOrgClient("some_org")

        has_license = github_org_client.has_license(repo, license_key)

        self.assertEqual(has_license, expected)

    
    @parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0], "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2], "apache2_repos": TEST_PAYLOAD[0][3]}
    ])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """CLASS - tests 'public_repos' in the 'GithubOrgClient'
        """

    @classmethod
    def setUpClass(cls):
        """ Integration testing class
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            if url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """METHOD - "tears down" the used class from integration testing
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """tests public repos without a license
        """
        test_client = GithubOrgClient("google")
        result = test_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """tests public repos with a license
        """
        test_client = GithubOrgClient("google")
        result = test_client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)

