#!/usr/bin/env python3

"""
Function that returns a tuple containing the string and the square of v.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a tuple containing the string and the square of v.
    v can be either ints or floats
    """

    return (k, v ** 2.0)
