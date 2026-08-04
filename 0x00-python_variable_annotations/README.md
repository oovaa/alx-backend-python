# 0x00-python_variable_annotations — Type Hints & Static Analysis

[![ALX](https://img.shields.io/badge/ALX-Backend%20Python-blue?style=flat-square&logo=python&logoColor=white)](https://www.alxafrica.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![mypy](https://img.shields.io/badge/mypy-type%20checking-blue.svg)]()

> **Python Variable Annotations** — Type hints for variables, functions, and complex types using `typing` module. Validated with `mypy`.

---

## 🎯 Overview

This project covers Python 3 type annotation syntax for variables, function signatures, and complex generic types. All exercises are validated with `mypy` strict mode.

---

## 📁 Files

| File | Description |
|------|-------------|
| `0-add.py` | Function `add(a: float, b: float) -> float` — basic type hints |
| `1-concat.py` | Function `concat(str1: str, str2: str) -> str` — string concatenation |
| `2-floor.py` | Function `floor(n: float) -> int` — using `math.floor` with annotations |
| `3-to_str.py` | Function `to_str(n: float) -> str` — float to string |
| `4-define_variables.py` | Annotated variable definitions: `a: int`, `pi: float`, `school: str`, `flag: bool` |
| `5-sum_list.py` | Function `sum_list(input_list: List[float]) -> float` — List type |
| `6-sum_mixed_list.py` | Function `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float` — Union type |
| `7-to_kv.py` | Function `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` — Tuple return |
| `8-make_multiplier.py` | Function `make_multiplier(multiplier: float) -> Callable[[float], float]` — Callable type |
| `9-element_length.py` | Function `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` — Iterable/Sequence |
| `100-safe_first_element.py` | Function `safe_first_element(lst: Sequence[Any]) -> Optional[Any]` — Optional |
| `101-safely_get_value.py` | Function `safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]` — Mapping, Generics |
| `102-type_checking.py` | Type checking with `TYPE_CHECKING` for circular imports |

---

## 🚀 Usage

```bash
# Run mypy on any file
mypy 0-add.py
mypy 5-sum_list.py
mypy 101-safely_get_value.py

# Run with strict mode
mypy --strict 0-add.py
```

---

## 🧪 Running Tests

Each file has a corresponding `*-main.py` test file:

```bash
python3 0-main.py   # Test add function
python3 1-main.py   # Test concat
python3 2-main.py   # Test floor
python3 3-main.py   # Test to_str
python3 4-main.py   # Test variable definitions
python3 5-main.py   # Test sum_list
python3 6-main.py   # Test sum_mixed_list
python3 7-main.py   # Test to_kv
python3 8-main.py   # Test make_multiplier
python3 9-main.py   # Test element_length
python3 100-main.py # Test safe_first_element
python3 101-main.py # Test safely_get_value
```

---

## 📚 Key Concepts

| Concept | Example |
|---------|---------|
| **Basic types** | `x: int = 5`, `name: str = "hello"` |
| **Function signatures** | `def add(a: float, b: float) -> float:` |
| **Container types** | `List[float]`, `Dict[str, int]`, `Tuple[str, float]` |
| **Union types** | `Union[int, float]`, `Optional[str]` (shorthand for `Union[str, None]`) |
| **Callable** | `Callable[[float], float]` — function taking float, returning float |
| **Iterable/Sequence** | `Iterable[Sequence]` — generic iterable of sequences |
| **Mapping** | `Mapping` — read-only dict-like interface |
| **Generics** | `TypeVar('T')` — for generic functions |
| **TYPE_CHECKING** | `if TYPE_CHECKING: import ...` — imports only for type checkers |

---

## 📚 Learning Outcomes

- ✅ Annotate variables, parameters, and return types
- ✅ Use `typing` module: `List`, `Dict`, `Tuple`, `Union`, `Optional`, `Callable`, `Iterable`, `Sequence`, `Mapping`, `Any`
- ✅ Define generic functions with `TypeVar`
- ✅ Handle circular imports with `TYPE_CHECKING`
- ✅ Validate types with `mypy --strict`

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)