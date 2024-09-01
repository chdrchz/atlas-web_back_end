#!/usr/bin/env python3
"""
Module that contains a function call imported function
n times and calculate the delay between each
"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine to call imported function n times and calculate
    delay between each

    Args:
        n: any int > 0
        max_delay: any int > 0

    Return:
        list of floats
    """

    # Calling task_wait_random n times
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Empty list for delays
    delays = []

    # Iterate over all tasks and calculate the delay
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
