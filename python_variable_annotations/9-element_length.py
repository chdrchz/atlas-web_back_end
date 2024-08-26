#!/usr/bin/env python3
"""
Function that finds the length of every element in list
"""
from typing import List, Tuple, Iterable, Any


def element_length(lst: List[Iterable[Any]]) -> List[Tuple[Iterable[Any], int]]:
    """
    Function that finds the length of every element in list
    """

    return [(i, len(i)) for i in lst]
