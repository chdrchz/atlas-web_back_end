#!/usr/bin/env python3
"""
Module that contains a coroutine that calls a coroutine
to loop 10 times and return 10 random numbers
"""

import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """
    Coroutine that calls a coroutine
    to loop 10 times and return 10 random numbers

    Args:
        none

    Return:
        List of floats
    """
    # Calculate start time
    start_time = time.perf_counter()

    # Call async comprehension 4 times in parallel
    tasks = [async_comprehension() for _ in range(4)] 

    # Await the task completions
    await asyncio.gather(*tasks)

    # Calculate end time and return difference
    return time.perf_counter() - start_time