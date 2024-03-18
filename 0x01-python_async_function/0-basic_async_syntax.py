#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
using random module.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine
    """
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
