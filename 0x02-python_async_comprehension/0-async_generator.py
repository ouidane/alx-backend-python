#!/usr/bin/env python3
""" generator coroutine that yields 10 random floats between 0 and 10. """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yield a random float between 0 and 10. """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
