#!/usr/bin/env python3
"""Function with proper type annotations using TypeVar."""

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Returns the value in a dictionary for a given key."""
    if key in dct:
        return dct[key]
    else:
        return default
