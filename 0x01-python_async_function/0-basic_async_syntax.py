#!/usr/bin/env python3
"""task 0"""


from random import random


async def wait_random(max_delay=10):
    d = random(max_delay)
    return d


print(wait_random())
