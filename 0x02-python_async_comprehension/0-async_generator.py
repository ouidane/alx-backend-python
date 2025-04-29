#!/usr/bin/env python3
"""Async generator coroutine that yields 10 random floats between 0 and 10.
"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Yield a random float between 0 and 10
    10 times with 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
