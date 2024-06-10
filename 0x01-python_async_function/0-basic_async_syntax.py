#!/usr/bin/env python3
'''
    The basics of async.
'''

from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    d = uniform(0, max_delay)
    await sleep(d)

    return d
