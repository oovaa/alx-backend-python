#!/usr/bin/env python3

'''
unittest access_nested_map
'''

import unittest
from unittest.mock import MagicMock, Mock
from aiohttp import payload_type
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize

# The test case


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload,  mocked_get):
        """ Test for the utils.get_json function to check
        that it returns the expected result."""
        mock_res = Mock()
        mock_res.json.return_value = test_payload  # Corrected typo here

        mocked_get.return_value = mock_res  # Corrected typo here

        test_get = get_json(test_url)

        self.assertEqual(test_get, test_payload)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function.

        Args:
        nested_map (dict): The nested map to access.
            path (list): The path to the desired value.
            expected: The expected value.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test case to verify that accessing a nested map with an invalid path
        raises a KeyError.

        Args:
            nested_map (dict): The nested map to access.
            path (list): The path to the desired value in the nested map.
            expected: The expected result.

        Raises:
            AssertionError: If the KeyError is not raised.

        Returns:
            None
        """
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(nested_map, path)
