#!/usr/bin/env python3

'''
task 0
'''

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """ Async Generator """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
