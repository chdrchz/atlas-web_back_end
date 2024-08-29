#!/usr/bin/env python3

"""
Coroutine that takes a max_delay as an argument, and randomly generates
 a number to wait to complete the asynchronous operation.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that takes a max_delay as an argument, and randomly generates
    a number to wait to complete the asynchronous operation.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
