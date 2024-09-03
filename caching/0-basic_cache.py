#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCaching defines:
        -adds an item to cache_data
        -retrieves an item from cache_data
    """
    def put(self, key, item):
        """ Adds an item to cache_data

            Args:
            -self: Instance of class
            -key: key for item
            -item: item to be added to cache_data

            Return:
            -None
        """

        # Prevent empty values from being added to cache_data
        if key is None:
            return

        if item is None:
            return

        # Add item to cache_data, based on its key
        self.cache_data[key] = item

    def get(self, key):
        """ Gets an item from cache_data

            Args:
            -self: Instance of class
            -key: key for item

            Return:
            -item from cache_data, based on key
        """

        # Retrieve item in cache_data, based on its key
        return self.cache_data.get(key)
