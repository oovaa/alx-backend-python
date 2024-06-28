#!/usr/bin/env python3

'''
unittest access_nested_map
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


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
