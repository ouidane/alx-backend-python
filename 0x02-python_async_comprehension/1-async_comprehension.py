#!/usr/bin/env python3
""" Collects 10 random numbers from async_generator """
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """ Return a list of 10 random numbers collected """
    return [i async for i in async_generator()]
