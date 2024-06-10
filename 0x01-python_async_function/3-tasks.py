#!/usr/bin/env python3

'''
task 3
'''

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates a task that waits for a random amount of time.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        Task: A task that waits for a random amount of time.
    """
    return create_task(wait_random(max_delay))
