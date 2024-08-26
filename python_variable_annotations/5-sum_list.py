#!/usr/bin/env python3

"""
Function that returns a float of the sum of input_lists
"""


def sum_list(input_lists: list[float]) -> float:
    """
    Function that returns a float of the sum of input_lists
    """
    
    sum = 0;
    for num in input_lists: 
        sum += num
    return sum
