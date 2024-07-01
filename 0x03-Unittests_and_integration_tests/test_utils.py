#!/usr/bin/env python3

'''
unittest access_nested_map
'''

import unittest
from unittest.mock import Mock
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize

# The test case


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


class TestGetJson(unittest.TestCase):
    """Class for testing get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mocked_get):
        """Test that utils.get_json returns the expected result without
        making actual HTTP calls."""
        # Setup the mock to return the test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mocked_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        mocked_get.assert_called_once_with(test_url)

        # Assert that the result matches the test payload
        self.assertEqual(result, test_payload)


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
