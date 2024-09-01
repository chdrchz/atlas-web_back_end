#!/usr/bin/env python3
"""
Module that contains a function to calculate elapsed time
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Calculates elapsed time.

    Args:
        n: any int > 0
        max_delay: any int > 0
    
    Return: 
        total_time / n as a float
    """

    # Start the timer
    start_time = time.perf_counter()

    # Await the coroutine
    await wait_n(n, max_delay)

    # Calculate the total elapsed time
    total_time = time.perf_counter() - start_time

    # Return the average time per task
    return total_time / n
