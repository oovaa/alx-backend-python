# 0x02-python_async_comprehension — Async Generators & Comprehensions

[![ALX](https://img.shields.io/badge/ALX-Backend%20Python-blue?style=flat-square&logo=python&logoColor=white)](https://www.alxafrica.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![asyncio](https://img.shields.io/badge/asyncio-standard%20library-green.svg)]()

> **Async Generators & Comprehensions** — Asynchronous generators, async comprehensions, and type annotations for async iterables.

---

## 🎯 Overview

Covers Python's asynchronous generators (`async def` with `yield`), async comprehensions (`[x async for x in gen]`), and proper type annotations using `AsyncGenerator`, `AsyncIterable`, `Awaitable`.

---

## 📁 Files

| File | Description |
|------|-------------|
| `0-async_generator.py` | `async def async_generator() -> AsyncGenerator[float, None]` — yields random floats with `asyncio.sleep` |
| `1-async_comprehension.py` | `async def async_comprehension() -> List[float]` — uses `[x async for x in async_generator()]` to collect 10 values |
| `2-measure_runtime.py` | `async def measure_runtime() -> float` — measures total time to run `async_comprehension` 4 times concurrently |

---

## 🚀 Usage

```bash
python3 0-async_generator.py
python3 1-async_comprehension.py
python3 2-measure_runtime.py
```

---

## 🧪 Running Tests

```bash
python3 0-main.py   # Test async_generator
python3 1-main.py   # Test async_comprehension
python3 2-main.py   # Test measure_runtime
```

---

## 📚 Key Concepts

| Concept | Syntax | Example |
|---------|--------|---------|
| **Async generator** | `async def gen() -> AsyncGenerator[T, None]: yield x` | `async def async_generator() -> AsyncGenerator[float, None]:` |
| **Async comprehension** | `[x async for x in async_gen()]` | `results = [x async for x in async_generator()]` |
| **Async for loop** | `async for x in async_gen():` | `async for val in async_generator(): print(val)` |
| **Type annotation** | `AsyncGenerator[YieldType, SendType]` | `AsyncGenerator[float, None]` |

---

## 📚 Learning Outcomes

- ✅ Write async generators with `async def` + `yield`
- ✅ Use async comprehensions for collecting async iterator results
- ✅ Annotate async generators with `AsyncGenerator`
- ✅ Run multiple async comprehensions concurrently
- ✅ Understand async iteration protocol

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)