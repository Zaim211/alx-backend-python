#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """
    delays = []
    steps = []

    for x in range(n):
        step = wait_random(max_delay)
        steps.append(step)

    for step in asyncio.as_completed(steps):
        delay = await step
        delays.append(delay)

    return delays
