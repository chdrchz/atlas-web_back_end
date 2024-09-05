#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Finds the range of data to be displayed

            Args:
                - self
                - index: position
                - page_size: rows per page

            Return:
                - A Dict with:
                    - page_size
                    - page
                    - data: data from get_page
                    - next_page: the number of the next page
                    - prev_page: the number of the previous page
                    - total_pages: the total number of pages
        """
        # Make sure that index is an int < the dataset length
        assert isinstance(index, int) and index < len(self.dataset())

        start_index = index

        # Current page data
        current_page = []

        while len(current_page) < page_size and \
                start_index < len(self.dataset()):

            if start_index is not None:
                # Append rows to the current page
                current_page.append(start_index)
            start_index += 1

        # Set next_index to None if the length of dataset is reached
        # before current_page fills
        # And set next_index to the end of the page
        if start_index >= len(self.dataset()):
            next_index = None
        else:
            next_index = start_index

        data_dict = {
            "index": index,  # page start index
            "next_index": next_index,
            "page_size": len(current_page),
            "data": current_page
        }

        return data_dict
