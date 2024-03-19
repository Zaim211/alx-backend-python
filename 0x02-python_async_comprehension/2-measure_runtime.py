#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds
"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
import time


async def measure_runtime() -> float:
    """
    Measure the total of runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start
