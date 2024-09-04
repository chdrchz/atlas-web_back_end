#!/usr/bin/env python3
"""
Module that contains a function to calculate
start and end pagination indexes
"""

def index_range(page: int, page_size: int) -> tuple:
    """ Function that returns a size 2 tuple containing the
        range of indexes possible with the pagination parameters

        Args:
            - page: page number to paginate
            - page_size: number of elements to display per page
        
        Return:
            - tuple conatining the start and end indexes
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return [start_index, end_index]
