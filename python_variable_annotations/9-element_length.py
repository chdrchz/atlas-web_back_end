#!/usr/bin/env python3
"""
Function that finds the length of every element in list
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that finds the length of every element in list
    """

    return [(i, len(i)) for i in lst]
