#!/usr/bin/env python3

"""
This function takes a float and returns a function that multiplies
the original argument with itself
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float and returns a function that multiplies
    the original argument with itself
    """
    def multiplier_function(val: float) -> float:
        """
        The multiplier function that multiplies multiplier with itself
        """
        return val * multiplier

    return multiplier_function