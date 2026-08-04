# 0x03-Unittests_and_integration_tests — Testing Strategies

[![ALX](https://img.shields.io/badge/ALX-Backend%20Python-blue?style=flat-square&logo=python&logoColor=white)](https://www.alxafrica.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![pytest](https://img.shields.io/badge/pytest-testing-green.svg)]()
[![unittest](https://img.shields.io/badge/unittest-standard%20library-blue.svg)]()

> **Unit & Integration Testing** — `unittest`, `pytest`, mocking, parameterized tests, and integration testing for async HTTP clients.

---

## 🎯 Overview

Covers comprehensive testing strategies: unit tests with `unittest`, mocking with `unittest.mock`, parameterized tests, async testing, and integration tests for a GitHub API client.

---

## 📁 Files

| File | Description |
|------|-------------|
| `utils.py` | Utility functions: `access_nested_map`, `get_json`, `memoize` |
| `test_utils.py` | Unit tests for `utils.py` — `TestAccessNestedMap`, `TestGetJson`, `TestMemoize` |
| `client.py` | `GithubOrgClient` — async client for GitHub org/repo API |
| `test_client.py` | Integration tests for `GithubOrgClient` — fixtures, mocking, parameterized |
| `TestGetJson.py` | Additional tests for `get_json` |
| `fixtures.py` | Test fixtures for GitHub API responses |
| `test_practice.py` | Practice test examples |
| `test_redo.py` | Additional test exercises |

---

## 🚀 Usage

```bash
# Run all tests with pytest
pytest -v

# Run specific test module
pytest test_utils.py -v
pytest test_client.py -v

# Run with coverage
pytest --cov=utils --cov=client
```

---

## 🧪 Key Test Patterns

### Unit Tests (`test_utils.py`)
```python
# Parameterized tests
@parameterized.expand([
    ({"a": 1}, ("a",), 1),
    ({"a": {"b": 2}}, ("a", "b"), 2),
])
def test_access_nested_map(self, nested_map, path, expected):
    self.assertEqual(access_nested_map(nested_map, path), expected)

# Mocking external calls
@patch('utils.get_json')
def test_get_json(self, mock_get_json):
    mock_get_json.return_value = {"payload": True}
    self.assertEqual(get_json("http://example.com"), {"payload": True})

# Testing memoization
def test_memoize(self):
    class TestClass:
        @memoize
        def a_method(self):
            return 42
    # Verify cached result
```

### Integration Tests (`test_client.py`)
```python
# Class-level fixtures
@parameterized_class([
    {"org_payload": ORG_PAYLOAD, "repos_payload": REPOS_PAYLOAD, "expected_repos": EXPECTED_REPOS, "apache2_repos": APACHE2_REPOS}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        # Configure mock responses...

    def test_public_repos(self):
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
```

---

## 📚 Learning Outcomes

- ✅ Write unit tests with `unittest.TestCase`
- ✅ Use `@parameterized.expand` for data-driven tests
- ✅ Mock external dependencies with `unittest.mock.patch`
- ✅ Test async code and memoization decorators
- ✅ Write integration tests with class-level fixtures
- ✅ Organize test fixtures for API client testing

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)