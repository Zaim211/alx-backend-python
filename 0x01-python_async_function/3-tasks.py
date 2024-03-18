#!/usr/bin/env python3
"""
Function that takes an integer max_delay and returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """
    takes an integer max_delay
    and returns a asyncio.Task
    """
    asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return asyncio.Task
