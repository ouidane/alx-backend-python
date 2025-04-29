#!/usr/bin/env python3
""" Measures the runtime of running async_comprehension four times """
import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel
    and return the total runtime.
    """
    start = time.time()
    tasks: List[asyncio.Task] = []
    for _ in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
