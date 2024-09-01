#!/usr/bin/env python3
"""
Module that contains a function to return a Task object
"""

import time
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns wait_random as an individual task

    Args:
        max_delay: any int > 0
    
    Return: 
        wait_random as an asyncio.Task object
    """
    # Returns the wait_random coroutine as a manipulatable task
    return asyncio.create_task(wait_random(max_delay))
