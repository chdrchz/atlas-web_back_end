#!/usr/bin/env python3
""" Module that contains a class that tests utils.py
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class that tests utils.py
    """
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests the access_nested_map function
            for expected vs actual

        Args:
            nested_map (_type_): Data to be iterated over
            path (_type_): Specific path to search in the nested map
            expected (_type_): The expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        """ Tests the access_nested_ap function for key

        Args:
            nested_map (_type_): Data to be iterated over
            path (_type_): Specific path to search in the nested map
            expected_exception_message (_type_): "Key 'a' not found in nested map"
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
