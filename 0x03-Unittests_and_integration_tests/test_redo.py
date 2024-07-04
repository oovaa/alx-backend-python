import unittest
from unittest.mock import patch

from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, moked):
        moked.return_value = {'name': org_name}
        client = GithubOrgClient(org_name)
        org_res = client.org

        self.assertEqual(org_res, {'name': org_name})


if __name__ == '__main__':
    unittest.main()
