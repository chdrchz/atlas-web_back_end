#!/usr/bin/env python3
"""
Module that contains a function to calculate
start and end pagination indexes
"""

import csv
import math
from typing import Any, List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Finds the range of data to be displayed

            Args:
                - self
                - page: current page
                - page_size: data size

            Return:
                - List of lists
        """
        # Make sure that the args are ints > 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Grab that data and add it to the indexes
        start_index, end_index = index_range(page, page_size)

        # Is the data within bounds? If yes, return an empty list
        data = self.dataset()
        if start_index >= len(data):
            return []

        # Return the appropriate range
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[Any, Any]:
        """ Finds the range of data to be displayed

            Args:
                - self
                - page: current page
                - page_size: data size

            Return:
                - A Dict with:
                    - page_size
                    - page
                    - data: data from get_page
                    - next_page: the number of the next page
                    - prev_page: the number of the previous page
                    - total_pages: the total number of pages
        """

        data_dict = {}

        # Grab that data
        data = self.get_page(page, page_size)
        data_dict['data'] = data

        # Total pages
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data_dict['total_pages'] = total_pages

        data_dict['page'] = page
        data_dict['page_size'] = page_size

        # Determine the previous page
        data_dict['prev_page'] = page - 1 if page > 1 else None

        # Determine the next page
        data_dict['next_page'] = page + 1 if page < total_pages else None

        return data_dict
