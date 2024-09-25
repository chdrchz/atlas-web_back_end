#!/usr/bin/env python3

import unittest
from unittest.mock import PropertyMock, patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        client = GithubOrgClient(org_name)

        # Call the method
        client.org

        mock_get.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
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
