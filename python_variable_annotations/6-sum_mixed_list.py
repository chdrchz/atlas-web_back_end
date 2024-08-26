#!/usr/bin/env python3

"""
Function that returns a float of the sum of input_list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function that returns a float of the sum of input_lists.
    The list will contain both ints and floats 
    """

    sum = 0
    for num in mxd_list:
        sum += num
    return sum
