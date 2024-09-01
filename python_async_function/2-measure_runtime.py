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

    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_taken: float = time.time()
    return time_taken - start_time
