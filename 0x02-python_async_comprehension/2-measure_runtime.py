#!/usr/bin/env python3

'''
task 2
'''

from asyncio import gather
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    return time() - start
