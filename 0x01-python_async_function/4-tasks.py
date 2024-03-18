#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """
    delays = []
    steps = []

    for x in range(n):
        step = task_wait_random(max_delay)
        steps.append(step)

    for step in asyncio.as_completed(steps):
        delay = await step
        delays.append(delay)

    return delays
