#!/usr/bin/env python3
""" Measures the runtime of running async_comprehension four times """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run async_comprehension four times in parallel """
    start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return (end - start)
