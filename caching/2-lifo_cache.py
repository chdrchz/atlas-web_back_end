#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCaching defines:
        - adds an item to cache_data, utilizes FIFO
        - retrieves an item from cache_data
    """

    def __init__(self):
        """ Initialization from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to cache_data

            Args:
            - self: Instance of class
            - key: key for item
            - item: item to be added to cache_data

            Return:
            - None
        """

        # Prevent empty values from being added to cache_data
        if key is None:
            return

        if item is None:
            return

        # Add item to cache_data, based on its key
        self.cache_data[key] = item

        # Remove the first item if the dictionary is greater than 4
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # iter() is like a loop, creates an iterable object
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """ Gets an item from cache_data

            Args:
            - self: Instance of class
            - key: key for item

            Return:
            - item from cache_data, based on key
            - None if key is none, or if key doesn't exist
        """

        # If they key exists
        if key is None:
            return None

        return self.cache_data.get(key)
