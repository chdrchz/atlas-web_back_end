#!/usr/bin/env python3
""" Module that contains a class Cache
"""

import redis
import uuid
from typing import Union


class Cache: 
    """ Class Cache
    """

    def __init__(self):
        """ init method
        """
        # Redis connection iunstance
        self._redis = redis.Redis()

        # Flush the database
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid and stores the key in redis

        Args:
            data (_type_): data to be stored with key

        Returns:
            str: a key
        """
        # Get the key
        key = str(uuid.uuid4())

        # Store the key
        # Returning here causes a bool response
        self._redis.set(key, data)

        return key
