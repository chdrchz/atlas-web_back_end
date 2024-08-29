#!/usr/bin/env python3
"""
Coroutine to call imported function n times and calculate
delay between each
"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine to call imported function n times and calculate
    delay between each
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
