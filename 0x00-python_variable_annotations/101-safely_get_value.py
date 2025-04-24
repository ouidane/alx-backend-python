#!/usr/bin/env python3
"""Function with proper type annotations using TypeVar."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, 
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns a value in a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
