#!/usr/bin/env python3
"""
Module that contains a coroutine that calls a coroutine
to loop 10 times and return 10 random numbers
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that calls a coroutine
    to loop 10 times and return 10 random numbers

    Args:
        none

    Return:
        List of floats
    """
    # async for is a for loop just for async coroutines
    numbers = [num async for num in async_generator()]

    return numbers