# 0x01-python_async_function — Asynchronous Programming

[![ALX](https://img.shields.io/badge/ALX-Backend%20Python-blue?style=flat-square&logo=python&logoColor=white)](https://www.alxafrica.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![asyncio](https://img.shields.io/badge/asyncio-standard%20library-green.svg)]()

> **Async/Await in Python** — Coroutines, concurrent execution, asyncio tasks, and runtime measurement.

---

## 🎯 Overview

Covers Python's `async`/`await` syntax, `asyncio` event loop, running coroutines concurrently with `asyncio.gather`, creating tasks with `asyncio.create_task`, and measuring async execution time.

---

## 📁 Files

| File | Description |
|------|-------------|
| `0-basic_async_syntax.py` | Basic coroutine `async def wait_random(max_delay: int = 10) -> float` — sleeps random delay, returns actual delay |
| `1-concurrent_coroutines.py` | `async def wait_n(n: int, max_delay: int) -> List[float]` — runs `wait_random` n times concurrently with `asyncio.gather` |
| `2-measure_runtime.py` | `def measure_time(n: int, max_delay: int) -> float` — measures total runtime of `wait_n` using `time.perf_counter` |
| `3-tasks.py` | `async def task_wait_n(n: int, max_delay: int) -> List[float]` — same as `wait_n` but using `asyncio.create_task` |
| `4-tasks.py` | `async def task_wait_random(max_delay: int) -> asyncio.Task` — returns a Task object |

---

## 🚀 Usage

```bash
# Run each module
python3 0-basic_async_syntax.py
python3 1-concurrent_coroutines.py
python3 2-measure_runtime.py
python3 3-tasks.py
python3 4-tasks.py
```

---

## 🧪 Running Tests

```bash
python3 0-main.py   # Test wait_random
python3 1-main.py   # Test wait_n
python3 2-main.py   # Test measure_time
python3 3-main.py   # Test task_wait_n
python3 4-main.py   # Test task_wait_random
```

---

## 📚 Key Concepts

| Concept | Example |
|---------|---------|
| **Coroutine** | `async def wait_random(max_delay) -> float:` |
| **Await** | `delay = await asyncio.sleep(random.uniform(0, max_delay))` |
| **Concurrent execution** | `await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))` |
| **Task creation** | `task = asyncio.create_task(coro())` |
| **Task vs Coroutine** | Task schedules immediately; coroutine awaits when called |
| **Runtime measurement** | `start = time.perf_counter(); ...; return time.perf_counter() - start` |

---

## 📚 Learning Outcomes

- ✅ Write async functions with `async def`
- ✅ Use `await` to suspend execution
- ✅ Run multiple coroutines concurrently with `asyncio.gather`
- ✅ Create and manage `asyncio.Task` objects
- ✅ Measure async code execution time accurately
- ✅ Understand difference between awaiting coroutines vs tasks

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)