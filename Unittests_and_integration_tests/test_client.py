#!/usr/bin/env python3

import unittest
from unittest.mock import patch
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
