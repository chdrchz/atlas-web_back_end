#!/usr/bin/env python3
"""
Module that contains a function to calculate elapsed time
"""

import time
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:

    # Returns the wait_random coroutine as a manipulatable task
    return asyncio.create_task(wait_random(max_delay))
