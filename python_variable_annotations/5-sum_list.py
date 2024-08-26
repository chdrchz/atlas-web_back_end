#!/usr/bin/env python3

"""
Function that returns a float of the sum of input_list
"""
from typing import List


def sum_list(input_list: list[float]) -> float:
    """
    Function that returns a float of the sum of input_lists
    """

    sum = 0;
    for num in input_list: 
        sum += num
    return sum
