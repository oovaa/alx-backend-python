import unittest
from unittest.mock import PropertyMock, patch

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
        moked.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, moked):
        moked.return_value = {
            "repos_url": 'https://github.com/oovaa/ccmdr'}
        client = GithubOrgClient('test')
        res = client._public_repos_url
        self.assertEqual(res, 'https://github.com/oovaa/ccmdr')


if __name__ == '__main__':
    unittest.main()
