from unittest.mock import MagicMock, patch
import unittest

from joke import get_joke, len_joke


class Testjoke(unittest.TestCase):

    @patch('joke.get_joke')
    def test_len_joke(self, moked):
        moked.return_value = 'one'

        self.assertEqual(len_joke(), 3)

    @patch('joke.requests')
    def test_get_joke(self, moked):
        moked_res = MagicMock()
        moked_res.status_code = 200
        moked_res.json.return_value = {'value': {'joke': 'one'}}

        moked.get.return_value = moked_res

        self.assertEqual(get_joke(), 'one')


if __name__ == '__main__':
    unittest.main()
