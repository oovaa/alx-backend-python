#!/usr/bin/env python3

'''
task 2
'''

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


import time
import asyncio

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of the wait_n function.

    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay for each call to the
        wait_n function.

    Returns:
        float: The average runtime of the wait_n function in seconds.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
