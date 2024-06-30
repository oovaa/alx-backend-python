import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


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


# class TestGetJson(unittest.TestCase):
#     """Class for Testing Get Json"""

#     @parameterized.expand([
#         ("http://example.com", {"payload": True}),
#         ("http://holberton.io", {"payload": False})
#     ])
#     @patch('requests.get')
#     def test_get_json(self, test_url, test_payload, mocked_get):
#         """Test for the utils.get_json function to check
#         that it returns the expected result."""
#         mock_res = Mock()
#         # Mock the json method to return the test payload
#         mock_res.json.return_value = test_payload

#         # Mock requests.get to return the mock response
#         mocked_get.return_value = mock_res

#         test_get = get_json(test_url)  # Call the function being tested

#         # Assert that the returned value matches the expected payload
#         self.assertEqual(test_get, test_payload)


if __name__ == '__main__':
    unittest.main()
