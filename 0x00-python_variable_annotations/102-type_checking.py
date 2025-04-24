#!/usr/bin/env python3
"""Function zoom_array with proper type annotations."""

from typing import List, Any

def zoom_array(lst: List[Any], factor: int = 2) -> List[Any]:
    """Return list of items from lst argument duplicated factor times"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
