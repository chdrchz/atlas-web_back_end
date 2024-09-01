#!/usr/bin/env python3
"""
Module that contains a coroutine that loops 10 times
"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loops ten times and yields a random number

    Args:
        none

    Return:
        random float
    """
    # Loop 10 times
    for _ in range(10):

        # Await 1 second in between
        await asyncio.sleep(1)

        # Yield a random int between 0 and 10 
        yield uniform(0, 10)
