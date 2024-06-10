#!/usr/bin/env python3

'''
task 1
'''


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    return [task.result() for task in completed_tasks]