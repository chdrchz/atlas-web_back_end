#!/usr/bin/env python3
"""
Module that contains a function to calculate elapsed time
"""

from time import perf_counter
from asyncio import run

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

    start_time = perf_counter()
    run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
